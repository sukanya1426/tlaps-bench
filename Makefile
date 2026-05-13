.PHONY: build clean

check_proof_bin: check_proof.py cheating_detection.py
	pyinstaller --onefile --name check_proof_bin check_proof.py
	mv dist/check_proof_bin ./check_proof_bin
	rm -rf dist/ build/ check_proof_bin.spec

build: check_proof_bin

clean:
	rm -f check_proof_bin
	rm -rf dist/ build/ *.spec
