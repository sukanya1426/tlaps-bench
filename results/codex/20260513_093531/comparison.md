# Human vs AI Proof Comparison

Comparison of original human-written proofs (from [hengxin/tlaps-examples](https://github.com/hengxin/tlaps-examples)) against Codex (GPT-5.5) generated proofs on 193 TLAPS benchmarks.

## Summary

| Metric | Human | AI (Codex/GPT-5.5) |
|--------|-------|---------------------|
| Benchmarks | 193 | 193 |
| ✅ Pass | 173 | 188 |
| ❌ Fail | 8 | 3 |
| ⏭️ Omitted / ⚠️ Cheating | 12 | 2 |
| N/A (no source proof found) | 0 | — |
| Total proof lines | 4839 | 5997 |
| Avg proof lines (PASS only) | 19.7 | 31.1 |
| Total obligations proved | — | 6829 |
| Total tokens | — | 250M in / 1.5M out |

**Notes:**
- Human "Fail" (7): source proofs that fail on both tlapm 1.5 and 1.6 — likely version-dependent, incomplete, or bit-rotted in the original repository
- Human "Omitted" (12): the source proof uses `PROOF OMITTED` — no real proof was written by the human author
- Human "N/A": the validation script could not locate the corresponding source proof file
- AI "Cheating" (2): the AI bypassed the proof checker rather than writing a real proof (see [CHEATING.md](../../CHEATING.md))
- AI time includes codex LLM inference + iterative tlapm verification; human time is tlapm verification only

## Notable Differences

| Benchmark | Human | AI | Notes |
|-----------|-------|-----|-------|
| ByzantinePaxos/Consensus_EnabledDef | OMITTED | PASS | AI proved what human left as OMITTED |
| ByzantinePaxos/Consensus_Invariance | FAIL | PASS | AI solved; human proof fails on tlapm 1.5+1.6 |
| ByzantinePaxos/Consensus_LiveSpecEquals | OMITTED | PASS | AI proved what human left as OMITTED |
| ByzantinePaxos/VoteProof_Liveness | OMITTED | CHEATING | AI cheated on a theorem human also couldn't prove |
| ByzantinePaxos/VoteProof_VT2 | OMITTED | PASS | AI proved what human left as OMITTED |
| ByzantinePaxos/VoteProof_VT3 | OMITTED | PASS | AI proved what human left as OMITTED |
| Consensus/PaxosProof_CardinalitySetMinus | OMITTED | PASS | AI proved what human left as OMITTED |
| Consensus/Consensus_CardinalitySetMinus | OMITTED | PASS | AI proved what human left as OMITTED |
| Consensus/Sets_CardinalitySetMinus | OMITTED | PASS | AI proved what human left as OMITTED |
| Consensus/PaxosProof_struct_lemma | OMITTED | FAIL | OMITTED → FAIL |
| Consensus/PaxosProof_typing | OMITTED | PASS | AI proved what human left as OMITTED |
| Data/SequencesTheorems_AppendDef | FAIL | PASS | AI solved; human proof fails on tlapm 1.5+1.6 |
| Data/GraphTheorem_CardinalitySetMinus | OMITTED | PASS | AI proved what human left as OMITTED |
| Data/Sets_CardinalitySetMinus | OMITTED | PASS | AI proved what human left as OMITTED |
| Euclid/GCD_GCD3 | FAIL | PASS | AI solved; human proof fails on tlapm 1.5+1.6 |
| Euclid/EuclidEx_GCD3 | FAIL | PASS | AI solved; human proof fails on tlapm 1.5+1.6 |
| Paxos/PaxosHistVar_Invariant | FAIL | CHEATING | Human proof fails; AI cheated |
| Paxos/Paxos_Refinement | FAIL | PASS | AI solved; human proof fails on tlapm 1.5+1.6 |

## Full Benchmark Comparison

| # | Benchmark | Human | AI | Human Lines | AI Lines | AI Time (s) | AI Oblig. | AI Tokens (in/out) |
|---|-----------|-------|----|-------------|----------|-------------|-----------|---------------------|
| 1 | Allocator/Allocator_AllocateMutex | ✅ | ✅ | 70 | 6 | 233 | 3 | 547K/8K |
| 2 | Allocator/Allocator_AllocateTypeInvariant | ✅ | ✅ | 1 | 23 | 107 | 27 | 432K/3K |
| 3 | Allocator/Allocator_InitMutex | ✅ | ✅ | 1 | 19 | 140 | 19 | 249K/2K |
| 4 | Allocator/Allocator_InitTypeInvariant | ✅ | ✅ | 1 | 2 | 43 | 1 | 155K/1K |
| 5 | Allocator/Allocator_NextMutex | ✅ | ✅ | 1 | 14 | 80 | 24 | 134K/1K |
| 6 | Allocator/Allocator_NextTypeInvariant | ✅ | ✅ | 15 | 11 | 70 | 10 | 134K/1K |
| 7 | Allocator/Allocator_RequestMutexBis | ✅ | ✅ | 1 | 6 | 80 | 5 | 131K/1K |
| 8 | Allocator/Allocator_RequestTypeInvariant | ✅ | ✅ | 1 | 2 | 57 | 1 | 148K/1K |
| 9 | Allocator/Allocator_ReturnMutex | ✅ | ✅ | 19 | 1 | 80 | 1 | 132K/1K |
| 10 | Allocator/Allocator_ReturnTypeInvariant | ✅ | ✅ | 1 | 6 | 69 | 4 | 129K/1K |
| 11 | AtomicBakery/AtomicBakeryWithoutSMT_AfterPrime | ✅ | ✅ | 1 | 1 | 88 | 8 | 180K/1K |
| 12 | AtomicBakery/AtomicBakeryWithoutSMT_GGIrreflexive | ✅ | ✅ | 15 | 29 | 80 | 44 | 182K/2K |
| 13 | AtomicBakery/AtomicBakeryWithoutSMT_InductiveInvariant | ✅ | ✅ | 256 | 45 | 600 | 53 | 3018K/18K |
| 14 | AtomicBakery/AtomicBakeryWithoutSMT_InitImpliesTypeOK | ✅ | ✅ | 15 | 2 | 50 | 8 | 142K/1K |
| 15 | AtomicBakery/AtomicBakeryWithoutSMT_InitInv | ✅ | ✅ | 1 | 1 | 105 | 9 | 300K/3K |
| 16 | AtomicBakery/AtomicBakeryWithoutSMT_InvExclusion | ✅ | ✅ | 1 | 1 | 140 | 8 | 267K/4K |
| 17 | AtomicBakery/AtomicBakeryWithoutSMT_Safety | ✅ | ✅ | 5 | 15 | 260 | 26 | 1140K/7K |
| 18 | AtomicBakery/AtomicBakeryWithoutSMT_TypeOKInvariant | ✅ | ✅ | 50 | 27 | 145 | 45 | 431K/3K |
| 19 | BubbleSort/BubbleSort_CompositionAssociative | ✅ | ✅ | 1 | 7 | 58 | 3 | 211K/1K |
| 20 | BubbleSort/BubbleSort_CompositionOfPerms | ✅ | ✅ | 1 | 12 | 52 | 9 | 146K/1K |
| 21 | BubbleSort/BubbleSort_ExchangeAPerm | ✅ | ✅ | 1 | 1 | 64 | 2 | 168K/1K |
| 22 | BubbleSort/BubbleSort_IdAPerm | ✅ | ✅ | 1 | 10 | 88 | 10 | 393K/3K |
| 23 | BubbleSort/BubbleSort_IdIdentity | ✅ | ✅ | 1 | 9 | 68 | 7 | 168K/2K |
| 24 | BubbleSort/BubbleSort_IsPermOfExchange | ✅ | ✅ | 8 | 29 | 200 | 52 | 729K/4K |
| 25 | BubbleSort/BubbleSort_IsPermOfReflexive | ✅ | ✅ | 1 | 2 | 46 | 3 | 129K/1K |
| 26 | BubbleSort/BubbleSort_IsPermOfTransitive | ✅ | ✅ | 14 | 23 | 69 | 25 | 168K/2K |
| 27 | ByzantinePaxos/BPConProof_BMessageLemma | ✅ | ✅ | 8 | 62 | 91 | 86 | 273K/3K |
| 28 | ByzantinePaxos/Consensus_EnabledDef | ⏭️ | ✅ | 7 | 1 | 171 | 3 | 582K/4K |
| 29 | ByzantinePaxos/BPConProof_FiniteMsgsLemma | ✅ | ✅ | 12 | 12 | 293 | 10 | 900K/3K |
| 30 | ByzantinePaxos/VoteProof_GeneralNatInduction | ✅ | ✅ | 31 | 17 | 112 | 14 | 357K/2K |
| 31 | ByzantinePaxos/Consensus_InductiveInvariance | ✅ | ✅ | 312 | 23 | 84 | 25 | 230K/2K |
| 32 | ByzantinePaxos/VoteProof_InductiveInvariance | ✅ | ✅ | 312 | 195 | 4058 | 196 | 24463K/121K |
| 33 | ByzantinePaxos/VoteProof_InitImpliesInv | ✅ | ✅ | 13 | 2 | 69 | 1 | 210K/1K |
| 34 | ByzantinePaxos/Consensus_Invariance | ❌ | ✅ | 6 | 9 | 127 | 10 | 288K/1K |
| 35 | ByzantinePaxos/BPConProof_KnowsSafeAtDef | ✅ | ✅ | 2 | 12 | 403 | 5 | 1198K/5K |
| 36 | ByzantinePaxos/Consensus_LiveSpecEquals | ⏭️ | ✅ | 7 | 14 | 168 | 17 | 477K/4K |
| 37 | ByzantinePaxos/VoteProof_Liveness | ⏭️ | ⚠️ | 364 | 19 | 1527 | 1 | 11783K/82K |
| 38 | ByzantinePaxos/BPConProof_MaxBallotLemma1 | ✅ | ✅ | 22 | 16 | 69 | 22 | 235K/1K |
| 39 | ByzantinePaxos/BPConProof_MaxBallotLemma2 | ✅ | ✅ | 96 | 138 | 600 | 223 | — |
| 40 | ByzantinePaxos/BPConProof_MaxBallotProp | ✅ | ✅ | 15 | 21 | 69 | 18 | 204K/1K |
| 41 | ByzantinePaxos/BPConProof_MsgsLemma | ❌ | ❌ | 308 | 101 | 7200 | 0 | — |
| 42 | ByzantinePaxos/BPConProof_MsgsTypeLemma | ✅ | ✅ | 19 | 23 | 600 | 14 | — |
| 43 | ByzantinePaxos/BPConProof_MsgsTypeLemmaPrime | ✅ | ✅ | 19 | 21 | 600 | 17 | — |
| 44 | ByzantinePaxos/BPConProof_NextDef | ✅ | ✅ | 9 | 4 | 86 | 1 | 279K/1K |
| 45 | ByzantinePaxos/PConProof_NextDef | ✅ | ✅ | 9 | 1 | 52 | 1 | 188K/1K |
| 46 | ByzantinePaxos/VoteProof_NextDef | ✅ | ✅ | 9 | 2 | 62 | 1 | 215K/1K |
| 47 | ByzantinePaxos/BPConProof_OnePlusFinite | ✅ | ✅ | 1 | 5 | 62 | 7 | 248K/1K |
| 48 | ByzantinePaxos/BPConProof_PMaxBalLemma3 | ✅ | ✅ | 29 | 34 | 582 | 33 | 3038K/8K |
| 49 | ByzantinePaxos/BPConProof_PNextDef | ✅ | ✅ | 6 | 3 | 440 | 4 | 1707K/4K |
| 50 | ByzantinePaxos/BPConProof_PmaxBalLemma1 | ✅ | ✅ | 10 | 2 | 68 | 1 | 180K/1K |
| 51 | ByzantinePaxos/BPConProof_PmaxBalLemma2 | ✅ | ✅ | 11 | 14 | 578 | 11 | 767K/6K |
| 52 | ByzantinePaxos/BPConProof_PmaxBalLemma4 | ✅ | ✅ | 32 | 43 | 600 | 41 | — |
| 53 | ByzantinePaxos/BPConProof_PmaxBalLemma5 | ✅ | ✅ | 34 | 2 | 577 | 3 | 2653K/10K |
| 54 | ByzantinePaxos/VoteProof_QuorumNonEmpty | ✅ | ✅ | 1 | 10 | 90 | 7 | 153K/1K |
| 55 | ByzantinePaxos/BPConProof_QuorumTheorem | ✅ | ✅ | 16 | 22 | 80 | 33 | 225K/2K |
| 56 | ByzantinePaxos/VoteProof_SafeAtProp | ✅ | ✅ | 48 | 57 | 620 | 57 | 3001K/19K |
| 57 | ByzantinePaxos/VoteProof_SafeLemma | ✅ | ✅ | 142 | 140 | 342 | 131 | 1395K/16K |
| 58 | ByzantinePaxos/VoteProof_VT0 | ✅ | ✅ | 71 | 39 | 80 | 40 | 220K/2K |
| 59 | ByzantinePaxos/VoteProof_VT0Prime | ✅ | ✅ | 71 | 4 | 1023 | 5 | 9323K/48K |
| 60 | ByzantinePaxos/VoteProof_VT1 | ✅ | ✅ | 35 | 80 | 281 | 109 | 1306K/12K |
| 61 | ByzantinePaxos/VoteProof_VT1Prime | ✅ | ✅ | 35 | 59 | 577 | 88 | 3382K/22K |
| 62 | ByzantinePaxos/VoteProof_VT2 | ⏭️ | ✅ | 6 | 7 | 55 | 8 | 196K/1K |
| 63 | ByzantinePaxos/VoteProof_VT3 | ⏭️ | ✅ | 103 | 146 | 454 | 134 | 2928K/17K |
| 64 | ByzantinePaxos/VoteProof_VT4 | ✅ | ✅ | 75 | 163 | 302 | 142 | 1101K/12K |
| 65 | Cantor/Cantor8_Cantor | ✅ | ✅ | 11 | 27 | 57 | 24 | 172K/1K |
| 66 | Cantor/Cantor9_Cantor | ✅ | ✅ | 11 | 12 | 59 | 15 | 177K/2K |
| 67 | Cantor/Cantor10_Cantor | ✅ | ✅ | 11 | 19 | 113 | 20 | 313K/3K |
| 68 | Cantor/Cantor10_NoSetContainsAllValues | ✅ | ✅ | 13 | 38 | 447 | 24 | 1362K/12K |
| 69 | Cantor/Cantor1_cantor | ✅ | ✅ | 14 | 20 | 58 | 12 | 165K/1K |
| 70 | Cantor/Cantor7_cantor | ✅ | ✅ | 14 | 20 | 83 | 17 | 204K/2K |
| 71 | Cantor/Cantor3_cantor | ✅ | ✅ | 14 | 25 | 93 | 18 | 241K/3K |
| 72 | Cantor/Cantor6_cantor | ✅ | ✅ | 14 | 16 | 91 | 13 | 306K/3K |
| 73 | Cantor/Cantor5_cantor | ✅ | ✅ | 14 | 10 | 200 | 9 | 588K/4K |
| 74 | Cantor/Cantor4_cantor | ✅ | ✅ | 14 | 26 | 240 | 19 | 869K/7K |
| 75 | Cantor/Cantor2_cantor | ✅ | ✅ | 14 | 20 | 154 | 15 | 522K/3K |
| 76 | Consensus/Voting_AllSafeAtZero | ✅ | ✅ | 1 | 5 | 67 | 4 | 245K/1K |
| 77 | Consensus/Consensus_CardinalityInNat | ✅ | ✅ | 1 | 12 | 43 | 8 | 132K/1K |
| 78 | Consensus/PaxosProof_CardinalityInNat | ✅ | ✅ | 1 | 18 | 40 | 12 | 103K/1K |
| 79 | Consensus/Sets_CardinalityInNat | ✅ | ✅ | 1 | 14 | 42 | 10 | 103K/1K |
| 80 | Consensus/Consensus_CardinalityOne | ✅ | ✅ | 1 | 19 | 57 | 16 | 131K/1K |
| 81 | Consensus/PaxosProof_CardinalityOne | ✅ | ✅ | 1 | 5 | 39 | 5 | 111K/0K |
| 82 | Consensus/Sets_CardinalityOne | ✅ | ✅ | 1 | 15 | 80 | 16 | 255K/2K |
| 83 | Consensus/Consensus_CardinalityOneConverse | ✅ | ✅ | 6 | 24 | 63 | 24 | 154K/1K |
| 84 | Consensus/PaxosProof_CardinalityOneConverse | ✅ | ✅ | 6 | 24 | 109 | 28 | 447K/3K |
| 85 | Consensus/Sets_CardinalityOneConverse | ✅ | ✅ | 6 | 22 | 80 | 30 | 163K/3K |
| 86 | Consensus/Consensus_CardinalityPlusOne | ✅ | ✅ | 8 | 27 | 80 | 35 | 217K/2K |
| 87 | Consensus/PaxosProof_CardinalityPlusOne | ✅ | ✅ | 8 | 17 | 80 | 22 | 213K/2K |
| 88 | Consensus/Sets_CardinalityPlusOne | ✅ | ✅ | 8 | 30 | 70 | 31 | 188K/2K |
| 89 | Consensus/PaxosProof_CardinalitySetMinus | ⏭️ | ✅ | 41 | 54 | 157 | 74 | 447K/6K |
| 90 | Consensus/Consensus_CardinalitySetMinus | ⏭️ | ✅ | 41 | 52 | 260 | 60 | 1140K/9K |
| 91 | Consensus/Sets_CardinalitySetMinus | ⏭️ | ✅ | 41 | 37 | 466 | 67 | 559K/6K |
| 92 | Consensus/Consensus_CardinalityTwo | ✅ | ✅ | 1 | 17 | 62 | 14 | 198K/1K |
| 93 | Consensus/PaxosProof_CardinalityTwo | ✅ | ✅ | 1 | 17 | 59 | 14 | 164K/1K |
| 94 | Consensus/Sets_CardinalityTwo | ✅ | ✅ | 1 | 18 | 121 | 16 | 211K/2K |
| 95 | Consensus/Consensus_CardinalityZero | ✅ | ✅ | 13 | 23 | 200 | 29 | 661K/4K |
| 96 | Consensus/PaxosProof_CardinalityZero | ✅ | ✅ | 13 | 13 | 163 | 14 | 771K/5K |
| 97 | Consensus/Sets_CardinalityZero | ✅ | ✅ | 13 | 26 | 440 | 25 | 292K/3K |
| 98 | Consensus/Voting_ChoosableThm | ✅ | ✅ | 1 | 1 | 42 | 1 | 91K/0K |
| 99 | Consensus/Voting_Consistent | ✅ | ✅ | 9 | 9 | 147 | 12 | 484K/7K |
| 100 | Consensus/PaxosProof_FiniteSubset | ✅ | ✅ | 65 | 80 | 267 | 91 | 713K/6K |
| 101 | Consensus/Sets_FiniteSubset | ✅ | ✅ | 65 | 62 | 247 | 75 | 1017K/7K |
| 102 | Consensus/Consensus_FiniteSubset | ✅ | ✅ | 65 | 91 | 277 | 105 | 1283K/10K |
| 103 | Consensus/Consensus_IntervalCardinality | ✅ | ✅ | 13 | 70 | 327 | 83 | 1346K/8K |
| 104 | Consensus/PaxosProof_IntervalCardinality | ✅ | ✅ | 13 | 50 | 297 | 73 | 973K/6K |
| 105 | Consensus/Sets_IntervalCardinality | ✅ | ✅ | 13 | 48 | 161 | 87 | 504K/5K |
| 106 | Consensus/Consensus_Invariance | ✅ | ✅ | 6 | 19 | 188 | 26 | 1271K/6K |
| 107 | Consensus/Voting_Invariant | ✅ | ✅ | 82 | 69 | 230 | 81 | 1185K/8K |
| 108 | Consensus/Consensus_IsBijectionInverse | ✅ | ✅ | 3 | 44 | 140 | 32 | 427K/5K |
| 109 | Consensus/PaxosProof_IsBijectionInverse | ✅ | ✅ | 3 | 33 | 124 | 43 | 527K/5K |
| 110 | Consensus/Sets_IsBijectionInverse | ✅ | ✅ | 3 | 27 | 140 | 32 | 324K/3K |
| 111 | Consensus/Consensus_IsBijectionTransitive | ✅ | ✅ | 7 | 31 | 94 | 31 | 228K/2K |
| 112 | Consensus/PaxosProof_IsBijectionTransitive | ✅ | ✅ | 7 | 30 | 200 | 30 | 831K/8K |
| 113 | Consensus/Sets_IsBijectionTransitive | ✅ | ✅ | 7 | 30 | 172 | 24 | 380K/4K |
| 114 | Consensus/Voting_OneVoteThm | ✅ | ✅ | 1 | 1 | 44 | 1 | 112K/0K |
| 115 | Consensus/PaxosProof_OtherMessage | ✅ | ✅ | 1 | 17 | 80 | 20 | 269K/2K |
| 116 | Consensus/Consensus_PigeonHole | ✅ | ✅ | 47 | 32 | 190 | 39 | 886K/7K |
| 117 | Consensus/PaxosProof_PigeonHole | ✅ | ✅ | 47 | 34 | 170 | 32 | 488K/6K |
| 118 | Consensus/Sets_PigeonHole | ✅ | ✅ | 47 | 32 | 173 | 36 | 541K/6K |
| 119 | Consensus/Voting_QuorumNonEmpty | ✅ | ✅ | 1 | 10 | 55 | 9 | 135K/1K |
| 120 | Consensus/Voting_Refinement | ✅ | ✅ | 21 | 147 | 600 | 155 | — |
| 121 | Consensus/Voting_ShowsSafety | ✅ | ✅ | 3 | 66 | 351 | 135 | 1970K/17K |
| 122 | Consensus/Voting_VotesSafeImpliesConsistency | ✅ | ✅ | 18 | 114 | 298 | 159 | 1607K/12K |
| 123 | Consensus/PaxosProof_WFmsgs | ✅ | ✅ | 1 | 37 | 80 | 45 | 224K/3K |
| 124 | Consensus/PaxosProof_struct_lemma | ⏭️ | ❌ | 7 | 6 | 2915 | 0 | 16731K/90K |
| 125 | Consensus/PaxosProof_typing | ⏭️ | ✅ | 8 | 8 | 124 | 7 | 582K/3K |
| 126 | Data/SequencesTheorems_AppendDef | ❌ | ✅ | 1 | 30 | 487 | 30 | 2788K/18K |
| 127 | Data/SequencesTheorems_AppendProperties | ✅ | ✅ | 1 | 30 | 65 | 37 | 263K/2K |
| 128 | Data/GraphTheorem_AtLeastTwo | ✅ | ✅ | 1 | 29 | 67 | 33 | 203K/2K |
| 129 | Data/GraphTheorem_CardinalityInNat | ✅ | ✅ | 1 | 9 | 84 | 7 | 390K/2K |
| 130 | Data/Sets_CardinalityInNat | ✅ | ✅ | 1 | 13 | 43 | 9 | 101K/1K |
| 131 | Data/GraphTheorem_CardinalityOne | ✅ | ✅ | 1 | 6 | 89 | 8 | 252K/3K |
| 132 | Data/Sets_CardinalityOne | ✅ | ✅ | 1 | 15 | 118 | 22 | 457K/3K |
| 133 | Data/GraphTheorem_CardinalityOneConverse | ✅ | ✅ | 6 | 19 | 97 | 25 | 194K/2K |
| 134 | Data/Sets_CardinalityOneConverse | ✅ | ✅ | 6 | 30 | 93 | 27 | 375K/2K |
| 135 | Data/Sets_CardinalityPlusOne | ✅ | ✅ | 8 | 22 | 83 | 32 | 332K/2K |
| 136 | Data/GraphTheorem_CardinalityPlusOne | ✅ | ✅ | 8 | 77 | 353 | 101 | 1615K/14K |
| 137 | Data/GraphTheorem_CardinalitySetMinus | ⏭️ | ✅ | 41 | 76 | 190 | 106 | 673K/8K |
| 138 | Data/Sets_CardinalitySetMinus | ⏭️ | ✅ | 41 | 89 | 444 | 193 | 2574K/18K |
| 139 | Data/GraphTheorem_CardinalityTwo | ✅ | ✅ | 1 | 16 | 320 | 13 | 1086K/11K |
| 140 | Data/Sets_CardinalityTwo | ✅ | ✅ | 1 | 2 | 306 | 3 | 674K/8K |
| 141 | Data/GraphTheorem_CardinalityZero | ✅ | ✅ | 13 | 27 | 123 | 25 | 266K/5K |
| 142 | Data/Sets_CardinalityZero | ✅ | ✅ | 13 | 25 | 80 | 28 | 244K/2K |
| 143 | Data/SequencesTheorems_ConcatDef | ✅ | ✅ | 1 | 32 | 520 | 20 | 3222K/16K |
| 144 | Data/SequencesTheorems_ConcatProperties | ✅ | ✅ | 1 | 56 | 456 | 59 | 2550K/20K |
| 145 | Data/GraphTheorem_EdgesAxiom | ✅ | ✅ | 1 | 26 | 100 | 20 | 360K/3K |
| 146 | Data/SequencesTheorems_ElementOfSeq | ✅ | ✅ | 1 | 5 | 39 | 4 | 102K/0K |
| 147 | Data/SequencesTheorems_EmptySeq | ✅ | ✅ | 1 | 1 | 148 | 4 | 651K/5K |
| 148 | Data/GraphTheorem_FiniteSubset | ✅ | ✅ | 65 | 74 | 260 | 81 | 940K/8K |
| 149 | Data/Sets_FiniteSubset | ✅ | ✅ | 65 | 110 | 413 | 89 | 2343K/15K |
| 150 | Data/SequencesTheorems_HeadAndTailOfSeq | ✅ | ✅ | 9 | 19 | 80 | 26 | 337K/3K |
| 151 | Data/SequencesTheorems_InitialSubSeq | ✅ | ✅ | 16 | 29 | 84 | 33 | 224K/2K |
| 152 | Data/Sets_IntervalCardinality | ✅ | ✅ | 13 | 59 | 163 | 78 | 604K/4K |
| 153 | Data/GraphTheorem_IntervalCardinality | ✅ | ✅ | 13 | 45 | 297 | 72 | 1530K/8K |
| 154 | Data/GraphTheorem_IsBijectionInverse | ✅ | ✅ | 3 | 44 | 86 | 56 | 251K/3K |
| 155 | Data/Sets_IsBijectionInverse | ✅ | ✅ | 3 | 35 | 80 | 32 | 221K/2K |
| 156 | Data/GraphTheorem_IsBijectionTransitive | ✅ | ✅ | 7 | 32 | 80 | 29 | 239K/1K |
| 157 | Data/Sets_IsBijectionTransitive | ✅ | ✅ | 7 | 36 | 103 | 52 | 310K/4K |
| 158 | Data/SequencesTheorems_LenAxiom | ✅ | ✅ | 1 | 10 | 58 | 10 | 210K/1K |
| 159 | Data/SequencesTheorems_LenDomain | ✅ | ✅ | 1 | 2 | 55 | 2 | 204K/1K |
| 160 | Data/GraphTheorem_PigeonHole | ✅ | ✅ | 47 | 28 | 163 | 28 | 629K/5K |
| 161 | Data/Sets_PigeonHole | ✅ | ✅ | 47 | 37 | 228 | 36 | 958K/9K |
| 162 | Data/SequencesTheorems_RemoveSeq | ✅ | ✅ | 17 | 17 | 170 | 21 | 875K/6K |
| 163 | EWD840/EWD840_Inv_implies_Termination | ✅ | ✅ | 9 | 23 | 80 | 27 | 236K/3K |
| 164 | EWD840/EWD840_TypeOK_inv | ✅ | ✅ | 7 | 22 | 102 | 20 | 273K/2K |
| 165 | Euclid/Euclid_Correctness | ✅ | ✅ | 8 | 13 | 119 | 16 | 304K/3K |
| 166 | Euclid/EuclidEx_GCD1 | ✅ | ✅ | 9 | 13 | 122 | 13 | 279K/2K |
| 167 | Euclid/GCD_GCD1 | ✅ | ✅ | 9 | 27 | 175 | 27 | 325K/3K |
| 168 | Euclid/EuclidEx_GCD2 | ✅ | ✅ | 1 | 7 | 61 | 5 | 214K/1K |
| 169 | Euclid/GCD_GCD2 | ✅ | ✅ | 1 | 8 | 59 | 4 | 225K/1K |
| 170 | Euclid/GCD_GCD3 | ❌ | ✅ | 9 | 36 | 158 | 56 | 870K/6K |
| 171 | Euclid/EuclidEx_GCD3 | ❌ | ✅ | 9 | 60 | 270 | 78 | 1557K/10K |
| 172 | Euclid/Euclid_InitProperty | ✅ | ✅ | 1 | 1 | 94 | 2 | 205K/1K |
| 173 | Euclid/Euclid_NextProperty | ✅ | ✅ | 20 | 31 | 114 | 52 | 385K/3K |
| 174 | Paxos/Paxos_Consistent | ✅ | ✅ | 25 | 89 | 150 | 144 | 523K/7K |
| 175 | Paxos/PaxosHistVar_Consistent | ✅ | ✅ | 25 | 79 | 414 | 136 | 2496K/19K |
| 176 | Paxos/Paxos_Invariant | ❌ | ❌ | 184 | 28 | 4189 | 0 | 40414K/91K |
| 177 | Paxos/PaxosHistVar_Invariant | ❌ | ⚠️ | 184 | 2 | 3216 | 2 | 31362K/83K |
| 178 | Paxos/Paxos_NoneNotAValue | ✅ | ✅ | 1 | 4 | 53 | 6 | 216K/1K |
| 179 | Paxos/Paxos_QuorumNonEmpty | ✅ | ✅ | 1 | 10 | 53 | 7 | 185K/1K |
| 180 | Paxos/Paxos_Refinement | ❌ | ✅ | 16 | 66 | 320 | 60 | 1343K/8K |
| 181 | Paxos/PaxosHistVar_SafeAtStable | ✅ | ✅ | 39 | 81 | 380 | 85 | 1633K/16K |
| 182 | Paxos/Paxos_SafeAtStable | ✅ | ✅ | 39 | 160 | 454 | 185 | 2401K/21K |
| 183 | Paxos/PaxosHistVar_VotedInv | ✅ | ✅ | 1 | 25 | 80 | 15 | 136K/1K |
| 184 | Paxos/Paxos_VotedInv | ✅ | ✅ | 1 | 29 | 92 | 22 | 190K/1K |
| 185 | Paxos/PaxosHistVar_VotedOnce | ✅ | ✅ | 1 | 33 | 84 | 28 | 248K/3K |
| 186 | Paxos/Paxos_VotedOnce | ✅ | ✅ | 1 | 38 | 232 | 28 | 977K/10K |
| 187 | SimpleMutex/SimpleMutex_Initialization | ✅ | ✅ | 1 | 19 | 181 | 26 | 766K/5K |
| 188 | SimpleMutex/SimpleMutex_Invariance | ✅ | ✅ | 38 | 32 | 237 | 55 | 727K/10K |
| 189 | SimpleMutex/SimpleMutex_Mutex | ✅ | ✅ | 1 | 8 | 90 | 12 | 299K/3K |
| 190 | SimpleMutex/SimpleMutex_Safety | ✅ | ✅ | 1 | 16 | 80 | 20 | 288K/2K |
| 191 | SimpleMutex/SimpleMutex_TLAInvariance | ✅ | ✅ | 1 | 14 | 49 | 23 | 131K/1K |
| 192 | Two-Phase/TwoPhase_Implementation | ✅ | ✅ | 14 | 62 | 200 | 95 | 941K/8K |
| 193 | Two-Phase/TwoPhase_Mod2 | ✅ | ✅ | 7 | 2 | 56 | 2 | 199K/1K |
