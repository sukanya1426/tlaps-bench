# TLAPS Benchmark Validation Report

**Generated**: 2026-05-14 00:34:02

## Summary

| Metric | Count |
|--------|-------|
| Total benchmarks | 193 |
| ✅ Passed | 174 |
| ❌ Failed | 7 |
| ⏭️ Placeholder (PROOF OMITTED) | 12 |
| 🔍 No proof found | 0 |
| 💥 Error | 0 |
| ⏱️ Total verification time | 1327.7s |
| 📝 Total baseline proof lines | 4469 |

## Results by Module

### Allocator (10/10 passed)

| Theorem | Source | Status | Proof Lines | Time | Notes |
|---------|--------|--------|-------------|------|-------|
| `AllocateMutex` | `Allocator/Allocator.tla` | ✅ PASS | 70 | 0.9s |  |
| `AllocateTypeInvariant` | `Allocator/Allocator.tla` | ✅ PASS | 1 | 0.3s |  |
| `InitMutex` | `Allocator/Allocator.tla` | ✅ PASS | 1 | 0.3s |  |
| `InitTypeInvariant` | `Allocator/Allocator.tla` | ✅ PASS | 1 | 0.3s |  |
| `NextMutex` | `Allocator/Allocator.tla` | ✅ PASS | 1 | 0.3s |  |
| `NextTypeInvariant` | `Allocator/Allocator.tla` | ✅ PASS | 15 | 0.3s |  |
| `RequestMutexBis` | `Allocator/Allocator.tla` | ✅ PASS | 1 | 0.3s |  |
| `RequestTypeInvariant` | `Allocator/Allocator.tla` | ✅ PASS | 1 | 0.3s |  |
| `ReturnMutex` | `Allocator/Allocator.tla` | ✅ PASS | 19 | 0.4s |  |
| `ReturnTypeInvariant` | `Allocator/Allocator.tla` | ✅ PASS | 1 | 0.3s |  |

### AtomicBakery (8/8 passed)

| Theorem | Source | Status | Proof Lines | Time | Notes |
|---------|--------|--------|-------------|------|-------|
| `AfterPrime` | `AtomicBakery/AtomicBakeryWithoutSMT.tla` | ✅ PASS | 1 | 0.9s |  |
| `GGIrreflexive` | `AtomicBakery/AtomicBakeryWithoutSMT.tla` | ✅ PASS | 15 | 0.8s |  |
| `InductiveInvariant` | `AtomicBakery/AtomicBakeryWithoutSMT.tla` | ✅ PASS | 256 | 23.8s |  |
| `InitImpliesTypeOK` | `AtomicBakery/AtomicBakeryWithoutSMT.tla` | ✅ PASS | 15 | 0.9s |  |
| `InitInv` | `AtomicBakery/AtomicBakeryWithoutSMT.tla` | ✅ PASS | 1 | 0.8s |  |
| `InvExclusion` | `AtomicBakery/AtomicBakeryWithoutSMT.tla` | ✅ PASS | 1 | 0.9s |  |
| `Safety` | `AtomicBakery/AtomicBakeryWithoutSMT.tla` | ✅ PASS | 5 | 1.0s |  |
| `TypeOKInvariant` | `AtomicBakery/AtomicBakeryWithoutSMT.tla` | ✅ PASS | 50 | 3.7s |  |

### BubbleSort (8/8 passed)

| Theorem | Source | Status | Proof Lines | Time | Notes |
|---------|--------|--------|-------------|------|-------|
| `CompositionAssociative` | `BubbleSort/BubbleSort.tla` | ✅ PASS | 1 | 0.3s |  |
| `CompositionOfPerms` | `BubbleSort/BubbleSort.tla` | ✅ PASS | 1 | 5.5s |  |
| `ExchangeAPerm` | `BubbleSort/BubbleSort.tla` | ✅ PASS | 1 | 0.3s |  |
| `IdAPerm` | `BubbleSort/BubbleSort.tla` | ✅ PASS | 1 | 0.3s |  |
| `IdIdentity` | `BubbleSort/BubbleSort.tla` | ✅ PASS | 1 | 0.3s |  |
| `IsPermOfExchange` | `BubbleSort/BubbleSort.tla` | ✅ PASS | 8 | 5.6s |  |
| `IsPermOfReflexive` | `BubbleSort/BubbleSort.tla` | ✅ PASS | 1 | 0.3s |  |
| `IsPermOfTransitive` | `BubbleSort/BubbleSort.tla` | ✅ PASS | 14 | 6.1s |  |

### ByzantinePaxos (31/38 passed)

| Theorem | Source | Status | Proof Lines | Time | Notes |
|---------|--------|--------|-------------|------|-------|
| `BMessageLemma` | `ByzantinePaxos/BPConProof.tla` | ✅ PASS | 8 | 0.4s |  |
| `EnabledDef` | `ByzantinePaxos/Consensus.tla` | ⏭️ OMITTED | 7 | 5.5s | PROOF_OMITTED: Proof uses PROOF OMITTED to skip obligations |
| `FiniteMsgsLemma` | `ByzantinePaxos/BPConProof.tla` | ✅ PASS | 12 | 90.1s |  |
| `GeneralNatInduction` | `ByzantinePaxos/VoteProof.tla` | ✅ PASS | 31 | 5.9s |  |
| `InductiveInvariance` | `ByzantinePaxos/Consensus.tla` | ✅ PASS | 15 | 5.5s |  |
| `InductiveInvariance` | `ByzantinePaxos/VoteProof.tla` | ✅ PASS | 312 | 13.1s |  |
| `InitImpliesInv` | `ByzantinePaxos/VoteProof.tla` | ✅ PASS | 13 | 0.8s |  |
| `Invariance` | `Consensus/Consensus.tla` | ❌ FAIL | 6 | 0.2s |  |
| `KnowsSafeAtDef` | `ByzantinePaxos/BPConProof.tla` | ✅ PASS | 2 | 93.6s |  |
| `LiveSpecEquals` | `ByzantinePaxos/Consensus.tla` | ⏭️ OMITTED | 7 | 0.2s | PROOF_OMITTED: Proof uses PROOF OMITTED to skip obligations |
| `Liveness` | `ByzantinePaxos/VoteProof.tla` | ⏭️ OMITTED | 364 | 26.0s | PROOF_OMITTED: Proof uses PROOF OMITTED to skip obligations |
| `MaxBallotLemma1` | `ByzantinePaxos/BPConProof.tla` | ✅ PASS | 22 | 1.1s |  |
| `MaxBallotLemma2` | `ByzantinePaxos/BPConProof.tla` | ✅ PASS | 96 | 4.3s |  |
| `MaxBallotProp` | `ByzantinePaxos/BPConProof.tla` | ✅ PASS | 15 | 1.0s |  |
| `MsgsLemma` | `ByzantinePaxos/BPConProof.tla` | ❌ FAIL | 308 | 120.0s | Timeout |
| `MsgsTypeLemma` | `ByzantinePaxos/BPConProof.tla` | ✅ PASS | 19 | 89.5s |  |
| `MsgsTypeLemmaPrime` | `ByzantinePaxos/BPConProof.tla` | ✅ PASS | 19 | 89.7s |  |
| `NextDef` | `ByzantinePaxos/PConProof.tla` | ✅ PASS | 8 | 0.5s |  |
| `NextDef` | `ByzantinePaxos/VoteProof.tla` | ✅ PASS | 7 | 0.8s |  |
| `NextDef` | `ByzantinePaxos/BPConProof.tla` | ✅ PASS | 9 | 7.3s |  |
| `OnePlusFinite` | `ByzantinePaxos/BPConProof.tla` | ✅ PASS | 1 | 5.3s |  |
| `PMaxBalLemma3` | `ByzantinePaxos/BPConProof.tla` | ✅ PASS | 29 | 93.3s |  |
| `PNextDef` | `ByzantinePaxos/BPConProof.tla` | ✅ PASS | 6 | 87.9s |  |
| `PmaxBalLemma1` | `ByzantinePaxos/BPConProof.tla` | ✅ PASS | 10 | 0.8s |  |
| `PmaxBalLemma2` | `ByzantinePaxos/BPConProof.tla` | ✅ PASS | 11 | 5.5s |  |
| `PmaxBalLemma4` | `ByzantinePaxos/BPConProof.tla` | ✅ PASS | 32 | 95.9s |  |
| `PmaxBalLemma5` | `ByzantinePaxos/BPConProof.tla` | ✅ PASS | 34 | 92.5s |  |
| `QuorumNonEmpty` | `ByzantinePaxos/VoteProof.tla` | ✅ PASS | 1 | 0.4s |  |
| `QuorumTheorem` | `ByzantinePaxos/BPConProof.tla` | ✅ PASS | 16 | 0.8s |  |
| `SafeAtProp` | `ByzantinePaxos/VoteProof.tla` | ✅ PASS | 48 | 11.4s |  |
| `SafeLemma` | `ByzantinePaxos/VoteProof.tla` | ✅ PASS | 142 | 8.9s |  |
| `VT0` | `ByzantinePaxos/VoteProof.tla` | ✅ PASS | 71 | 7.0s |  |
| `VT0Prime` | `ByzantinePaxos/VoteProof.tla` | ✅ PASS | 71 | 7.4s |  |
| `VT1` | `ByzantinePaxos/VoteProof.tla` | ✅ PASS | 35 | 1.3s |  |
| `VT1Prime` | `ByzantinePaxos/VoteProof.tla` | ✅ PASS | 35 | 1.5s |  |
| `VT2` | `ByzantinePaxos/VoteProof.tla` | ⏭️ OMITTED | 6 | 0.3s | PROOF_OMITTED: Proof uses PROOF OMITTED to skip obligations |
| `VT3` | `ByzantinePaxos/VoteProof.tla` | ⏭️ OMITTED | 103 | 10.4s | PROOF_OMITTED: Proof uses PROOF OMITTED to skip obligations |
| `VT4` | `ByzantinePaxos/VoteProof.tla` | ✅ PASS | 75 | 6.7s |  |

### Cantor (11/11 passed)

| Theorem | Source | Status | Proof Lines | Time | Notes |
|---------|--------|--------|-------------|------|-------|
| `Cantor` | `Cantor/Cantor8.tla` | ✅ PASS | 15 | 0.3s |  |
| `Cantor` | `Cantor/Cantor10.tla` | ✅ PASS | 6 | 0.3s |  |
| `Cantor` | `Cantor/Cantor9.tla` | ✅ PASS | 11 | 5.4s |  |
| `NoSetContainsAllValues` | `Cantor/Cantor10.tla` | ✅ PASS | 13 | 5.4s |  |
| `cantor` | `Cantor/Cantor7.tla` | ✅ PASS | 6 | 0.3s |  |
| `cantor` | `Cantor/Cantor6.tla` | ✅ PASS | 4 | 0.3s |  |
| `cantor` | `Cantor/Cantor5.tla` | ✅ PASS | 5 | 0.4s |  |
| `cantor` | `Cantor/Cantor3.tla` | ✅ PASS | 20 | 5.4s |  |
| `cantor` | `Cantor/Cantor2.tla` | ✅ PASS | 19 | 5.4s |  |
| `cantor` | `Cantor/Cantor1.tla` | ✅ PASS | 7 | 5.4s |  |
| `cantor` | `Cantor/Cantor4.tla` | ✅ PASS | 14 | 5.4s |  |

### Consensus (45/50 passed)

| Theorem | Source | Status | Proof Lines | Time | Notes |
|---------|--------|--------|-------------|------|-------|
| `AllSafeAtZero` | `Consensus/Voting.tla` | ✅ PASS | 1 | 0.5s |  |
| `CardinalityInNat` | `Consensus/Sets.tla` | ✅ PASS | 1 | 0.3s |  |
| `CardinalityInNat` | `Consensus/Sets.tla` | ✅ PASS | 1 | 0.6s |  |
| `CardinalityInNat` | `Data/Sets.tla` | ✅ PASS | 1 | 0.6s |  |
| `CardinalityOne` | `Consensus/Sets.tla` | ✅ PASS | 1 | 0.9s |  |
| `CardinalityOne` | `Consensus/Sets.tla` | ✅ PASS | 1 | 0.8s |  |
| `CardinalityOne` | `Data/Sets.tla` | ✅ PASS | 1 | 0.9s |  |
| `CardinalityOneConverse` | `Consensus/Sets.tla` | ✅ PASS | 6 | 5.5s |  |
| `CardinalityOneConverse` | `Consensus/Sets.tla` | ✅ PASS | 6 | 5.7s |  |
| `CardinalityOneConverse` | `Data/Sets.tla` | ✅ PASS | 6 | 5.5s |  |
| `CardinalityPlusOne` | `Consensus/Sets.tla` | ✅ PASS | 8 | 0.8s |  |
| `CardinalityPlusOne` | `Consensus/Sets.tla` | ✅ PASS | 8 | 0.9s |  |
| `CardinalityPlusOne` | `Data/Sets.tla` | ✅ PASS | 8 | 1.0s |  |
| `CardinalitySetMinus` | `Consensus/Sets.tla` | ⏭️ OMITTED | 41 | 1.2s | PROOF_OMITTED: Proof uses PROOF OMITTED to skip obligations |
| `CardinalitySetMinus` | `Consensus/Sets.tla` | ⏭️ OMITTED | 41 | 1.4s | PROOF_OMITTED: Proof uses PROOF OMITTED to skip obligations |
| `CardinalitySetMinus` | `Data/Sets.tla` | ⏭️ OMITTED | 41 | 1.5s | PROOF_OMITTED: Proof uses PROOF OMITTED to skip obligations |
| `CardinalityTwo` | `Consensus/Sets.tla` | ✅ PASS | 1 | 0.9s |  |
| `CardinalityTwo` | `Consensus/Sets.tla` | ✅ PASS | 1 | 0.8s |  |
| `CardinalityTwo` | `Data/Sets.tla` | ✅ PASS | 1 | 0.8s |  |
| `CardinalityZero` | `Consensus/Sets.tla` | ✅ PASS | 13 | 0.7s |  |
| `CardinalityZero` | `Consensus/Sets.tla` | ✅ PASS | 13 | 0.8s |  |
| `CardinalityZero` | `Data/Sets.tla` | ✅ PASS | 13 | 0.7s |  |
| `ChoosableThm` | `Consensus/Voting.tla` | ✅ PASS | 1 | 0.5s |  |
| `Consistent` | `Consensus/Voting.tla` | ✅ PASS | 9 | 0.6s |  |
| `FiniteSubset` | `Consensus/Sets.tla` | ✅ PASS | 65 | 1.8s |  |
| `FiniteSubset` | `Consensus/Sets.tla` | ✅ PASS | 65 | 2.1s |  |
| `FiniteSubset` | `Data/Sets.tla` | ✅ PASS | 65 | 1.8s |  |
| `IntervalCardinality` | `Consensus/Sets.tla` | ✅ PASS | 14 | 1.3s |  |
| `IntervalCardinality` | `Consensus/Sets.tla` | ✅ PASS | 14 | 1.5s |  |
| `IntervalCardinality` | `Data/Sets.tla` | ✅ PASS | 13 | 1.3s |  |
| `Invariance` | `Consensus/Consensus.tla` | ✅ PASS | 6 | 0.7s |  |
| `Invariant` | `Consensus/Voting.tla` | ✅ PASS | 82 | 13.5s |  |
| `IsBijectionInverse` | `Consensus/Sets.tla` | ✅ PASS | 3 | 0.6s |  |
| `IsBijectionInverse` | `Consensus/Sets.tla` | ✅ PASS | 3 | 0.6s |  |
| `IsBijectionInverse` | `Data/Sets.tla` | ✅ PASS | 3 | 0.5s |  |
| `IsBijectionTransitive` | `Consensus/Sets.tla` | ✅ PASS | 7 | 0.7s |  |
| `IsBijectionTransitive` | `Consensus/Sets.tla` | ✅ PASS | 7 | 0.7s |  |
| `IsBijectionTransitive` | `Data/Sets.tla` | ✅ PASS | 7 | 0.6s |  |
| `OneVoteThm` | `Consensus/Voting.tla` | ✅ PASS | 1 | 0.5s |  |
| `OtherMessage` | `Consensus/PaxosProof.tla` | ✅ PASS | 1 | 2.6s |  |
| `PigeonHole` | `Consensus/Sets.tla` | ✅ PASS | 47 | 1.7s |  |
| `PigeonHole` | `Consensus/Sets.tla` | ✅ PASS | 47 | 1.9s |  |
| `PigeonHole` | `Data/Sets.tla` | ✅ PASS | 47 | 1.9s |  |
| `QuorumNonEmpty` | `Consensus/Voting.tla` | ✅ PASS | 1 | 0.5s |  |
| `Refinement` | `Consensus/Voting.tla` | ✅ PASS | 21 | 2.6s |  |
| `ShowsSafety` | `Consensus/Voting.tla` | ✅ PASS | 3 | 4.3s |  |
| `VotesSafeImpliesConsistency` | `Consensus/Voting.tla` | ✅ PASS | 18 | 0.9s |  |
| `WFmsgs` | `Consensus/PaxosProof.tla` | ✅ PASS | 1 | 2.4s |  |
| `struct_lemma` | `Consensus/PaxosProof.tla` | ⏭️ OMITTED | 7 | 3.0s | PROOF_OMITTED: Proof uses PROOF OMITTED to skip obligations |
| `typing` | `Consensus/PaxosProof.tla` | ⏭️ OMITTED | 8 | 3.0s | PROOF_OMITTED: Proof uses PROOF OMITTED to skip obligations |

### Data (34/37 passed)

| Theorem | Source | Status | Proof Lines | Time | Notes |
|---------|--------|--------|-------------|------|-------|
| `AppendDef` | `Data/SequencesTheorems.tla` | ❌ FAIL | 1 | 5.5s | 1/2 obligations failed |
| `AppendProperties` | `Data/SequencesTheorems.tla` | ✅ PASS | 1 | 0.5s |  |
| `AtLeastTwo` | `Data/GraphTheorem.tla` | ✅ PASS | 1 | 0.6s |  |
| `CardinalityInNat` | `Data/Sets.tla` | ✅ PASS | 1 | 0.5s |  |
| `CardinalityInNat` | `Data/Sets.tla` | ✅ PASS | 1 | 0.7s |  |
| `CardinalityOne` | `Data/Sets.tla` | ✅ PASS | 1 | 0.9s |  |
| `CardinalityOne` | `Data/Sets.tla` | ✅ PASS | 1 | 1.0s |  |
| `CardinalityOneConverse` | `Data/Sets.tla` | ✅ PASS | 6 | 5.6s |  |
| `CardinalityOneConverse` | `Data/Sets.tla` | ✅ PASS | 6 | 5.8s |  |
| `CardinalityPlusOne` | `Data/Sets.tla` | ✅ PASS | 8 | 1.1s |  |
| `CardinalityPlusOne` | `Data/Sets.tla` | ✅ PASS | 8 | 1.1s |  |
| `CardinalitySetMinus` | `Data/Sets.tla` | ⏭️ OMITTED | 41 | 1.5s | PROOF_OMITTED: Proof uses PROOF OMITTED to skip obligations |
| `CardinalitySetMinus` | `Data/Sets.tla` | ⏭️ OMITTED | 41 | 1.5s | PROOF_OMITTED: Proof uses PROOF OMITTED to skip obligations |
| `CardinalityTwo` | `Data/Sets.tla` | ✅ PASS | 1 | 1.0s |  |
| `CardinalityTwo` | `Data/Sets.tla` | ✅ PASS | 1 | 0.9s |  |
| `CardinalityZero` | `Data/Sets.tla` | ✅ PASS | 13 | 0.8s |  |
| `CardinalityZero` | `Data/Sets.tla` | ✅ PASS | 13 | 0.8s |  |
| `ConcatDef` | `Data/SequencesTheorems.tla` | ✅ PASS | 1 | 0.4s |  |
| `ConcatProperties` | `Data/SequencesTheorems.tla` | ✅ PASS | 1 | 0.5s |  |
| `EdgesAxiom` | `Data/GraphTheorem.tla` | ✅ PASS | 1 | 1.1s |  |
| `ElementOfSeq` | `Data/SequencesTheorems.tla` | ✅ PASS | 1 | 0.6s |  |
| `EmptySeq` | `Data/SequencesTheorems.tla` | ✅ PASS | 1 | 0.5s |  |
| `FiniteSubset` | `Data/Sets.tla` | ✅ PASS | 65 | 2.3s |  |
| `FiniteSubset` | `Data/Sets.tla` | ✅ PASS | 65 | 2.0s |  |
| `HeadAndTailOfSeq` | `Data/SequencesTheorems.tla` | ✅ PASS | 9 | 0.7s |  |
| `InitialSubSeq` | `Data/SequencesTheorems.tla` | ✅ PASS | 16 | 2.2s |  |
| `IntervalCardinality` | `Data/Sets.tla` | ✅ PASS | 13 | 1.4s |  |
| `IntervalCardinality` | `Data/Sets.tla` | ✅ PASS | 13 | 1.3s |  |
| `IsBijectionInverse` | `Data/Sets.tla` | ✅ PASS | 3 | 0.7s |  |
| `IsBijectionInverse` | `Data/Sets.tla` | ✅ PASS | 3 | 0.5s |  |
| `IsBijectionTransitive` | `Data/Sets.tla` | ✅ PASS | 7 | 0.7s |  |
| `IsBijectionTransitive` | `Data/Sets.tla` | ✅ PASS | 7 | 0.7s |  |
| `LenAxiom` | `Data/SequencesTheorems.tla` | ✅ PASS | 1 | 0.7s |  |
| `LenDomain` | `Data/SequencesTheorems.tla` | ✅ PASS | 1 | 0.5s |  |
| `PigeonHole` | `Data/Sets.tla` | ✅ PASS | 47 | 2.0s |  |
| `PigeonHole` | `Data/Sets.tla` | ✅ PASS | 47 | 1.7s |  |
| `RemoveSeq` | `Data/SequencesTheorems.tla` | ✅ PASS | 17 | 0.9s |  |

### EWD840 (2/2 passed)

| Theorem | Source | Status | Proof Lines | Time | Notes |
|---------|--------|--------|-------------|------|-------|
| `Inv_implies_Termination` | `EWD840/EWD840.tla` | ✅ PASS | 9 | 0.8s |  |
| `TypeOK_inv` | `EWD840/EWD840.tla` | ✅ PASS | 7 | 0.4s |  |

### Euclid (7/9 passed)

| Theorem | Source | Status | Proof Lines | Time | Notes |
|---------|--------|--------|-------------|------|-------|
| `Correctness` | `Euclid/Euclid-TLAPS-Example/Euclid.tla` | ✅ PASS | 8 | 0.6s |  |
| `GCD1` | `Euclid/Euclid-Hyperbook/GCD.tla` | ✅ PASS | 9 | 0.7s |  |
| `GCD1` | `Euclid/Euclid-Hyperbook/GCD.tla` | ✅ PASS | 9 | 0.6s |  |
| `GCD2` | `Euclid/Euclid-Hyperbook/GCD.tla` | ✅ PASS | 1 | 0.5s |  |
| `GCD2` | `Euclid/Euclid-Hyperbook/GCD.tla` | ✅ PASS | 1 | 0.5s |  |
| `GCD3` | `Euclid/Euclid-Hyperbook/GCD.tla` | ❌ FAIL | 9 | 5.7s | 1/3 obligations failed |
| `GCD3` | `Euclid/Euclid-Hyperbook/GCD.tla` | ❌ FAIL | 9 | 5.8s | 1/3 obligations failed |
| `InitProperty` | `Euclid/Euclid-TLAPS-Example/Euclid.tla` | ✅ PASS | 1 | 0.5s |  |
| `NextProperty` | `Euclid/Euclid-TLAPS-Example/Euclid.tla` | ✅ PASS | 20 | 0.8s |  |

### Paxos (11/13 passed)

| Theorem | Source | Status | Proof Lines | Time | Notes |
|---------|--------|--------|-------------|------|-------|
| `Consistent` | `Paxos/Paxos.tla` | ✅ PASS | 25 | 1.0s |  |
| `Consistent` | `Paxos/PaxosHistVar.tla` | ✅ PASS | 25 | 1.4s |  |
| `Invariant` | `Paxos/PaxosHistVar.tla` | ✅ PASS | 126 | 7.1s |  |
| `Invariant` | `Paxos/Paxos.tla` | ❌ FAIL | 184 | 46.6s | 2/161 obligations failed |
| `NoneNotAValue` | `Paxos/Paxos.tla` | ✅ PASS | 1 | 0.5s |  |
| `QuorumNonEmpty` | `Paxos/Paxos.tla` | ✅ PASS | 1 | 0.5s |  |
| `Refinement` | `Paxos/Paxos.tla` | ❌ FAIL | 16 | 17.0s | 1/19 obligations failed |
| `SafeAtStable` | `Paxos/Paxos.tla` | ✅ PASS | 49 | 6.4s |  |
| `SafeAtStable` | `Paxos/PaxosHistVar.tla` | ✅ PASS | 39 | 1.2s |  |
| `VotedInv` | `Paxos/PaxosHistVar.tla` | ✅ PASS | 1 | 0.8s |  |
| `VotedInv` | `Paxos/Paxos.tla` | ✅ PASS | 1 | 0.7s |  |
| `VotedOnce` | `Paxos/PaxosHistVar.tla` | ✅ PASS | 1 | 0.7s |  |
| `VotedOnce` | `Paxos/Paxos.tla` | ✅ PASS | 1 | 0.7s |  |

### SimpleMutex (5/5 passed)

| Theorem | Source | Status | Proof Lines | Time | Notes |
|---------|--------|--------|-------------|------|-------|
| `Initialization` | `SimpleMutex/SimpleMutex.tla` | ✅ PASS | 1 | 0.5s |  |
| `Invariance` | `SimpleMutex/SimpleMutex.tla` | ✅ PASS | 38 | 2.5s |  |
| `Mutex` | `SimpleMutex/SimpleMutex.tla` | ✅ PASS | 1 | 0.5s |  |
| `Safety` | `SimpleMutex/SimpleMutex.tla` | ✅ PASS | 1 | 0.5s |  |
| `TLAInvariance` | `SimpleMutex/SimpleMutex.tla` | ✅ PASS | 1 | 0.5s |  |

### Two-Phase (2/2 passed)

| Theorem | Source | Status | Proof Lines | Time | Notes |
|---------|--------|--------|-------------|------|-------|
| `Implementation` | `Two-Phase/TwoPhase.tla` | ✅ PASS | 14 | 0.6s |  |
| `Mod2` | `Two-Phase/TwoPhase.tla` | ✅ PASS | 7 | 0.5s |  |

## Placeholder Proofs (PROOF OMITTED in source)

12 benchmarks have source proofs that use PROOF OMITTED.

## Failed Verification Details

### `benchmark/ByzantinePaxos/Consensus_Invariance.tla`

```
[INFO]: All 0 obligation proved.
[INFO]: All 0 obligation proved.
```

### `benchmark/ByzantinePaxos/BPConProof_MsgsLemma.tla`


### `benchmark/Data/SequencesTheorems_AppendDef.tla`

```
[INFO]: All 0 obligation proved.
[ERROR]: Could not prove or check:
[ERROR]: 1/2 obligations failed.
 tlapm ending abnormally with Failure("backend errors: there are unproved obligations")
```

### `benchmark/Euclid/EuclidEx_GCD3.tla`

```
[INFO]: All 0 obligation proved.
[ERROR]: Could not prove or check:
[ERROR]: 1/3 obligations failed.
 tlapm ending abnormally with Failure("backend errors: there are unproved obligations")
```

### `benchmark/Euclid/GCD_GCD3.tla`

```
[ERROR]: Could not prove or check:
[ERROR]: 1/3 obligations failed.
 tlapm ending abnormally with Failure("backend errors: there are unproved obligations")
```

### `benchmark/Paxos/Paxos_Invariant.tla`

```
[INFO]: All 0 obligation proved.
[ERROR]: Could not prove or check:
[ERROR]: Could not prove or check:
[ERROR]: 2/161 obligations failed.
 tlapm ending abnormally with Failure("backend errors: there are unproved obligations")
```

### `benchmark/Paxos/Paxos_Refinement.tla`

```
[INFO]: All 0 obligation proved.
[INFO]: All 0 obligation proved.
[ERROR]: Could not prove or check:
[ERROR]: 1/19 obligations failed.
 tlapm ending abnormally with Failure("backend errors: there are unproved obligations")
```
