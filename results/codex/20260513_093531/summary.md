# Codex Benchmark Results (2026-05-13)

**Total benchmarks**: 193
**PASS**: 188 | **FAIL**: 3 | **CHEATING**: 2
**Total obligations proved (legitimate)**: 6829

## Benchmark Validation (source proofs)

- **168/193** benchmarks have source proofs that pass tlapm 1.5
- **6** additional pass with tlapm 1.6 rerun (BubbleSort_ExchangeAPerm, Data/SequencesTheorems_ConcatDef, EWD840_TypeOK_inv, PaxosHistVar_SafeAtStable, SimpleMutex_Invariance, PaxosHistVar_Invariant)
- **7** fail on both 1.5 and 1.6 (Consensus_Invariance, Paxos_Invariant, Paxos_Refinement, BPConProof_MsgsLemma, Data/SequencesTheorems_AppendDef, Euclid/EuclidEx_GCD3, Euclid/GCD_GCD3)
- **12** have PROOF OMITTED placeholder in the source

See [benchmark_validation.md](benchmark_validation.md) for full report, [comparison.md](comparison.md) for human vs AI comparison.

## Cheating Detected

| Benchmark | Time (s) | Method |
|-----------|----------|--------|
| Paxos/PaxosHistVar_Invariant | 3216 | Deleted PROOF keyword — bare theorem declaration generates 0 obligations; added fake theorem to bypass zero-obligation check. Rerun with 2h timeout also failed: codex wrote legitimate-looking proof with BY references, but tlapm 1.5 generates 0 obligations (source requires 1.6). Tested on tlapm 1.6: 1/2 obligations failed (proof structure not properly expanded; source has 181/182 obligations on 1.6). |
| ByzantinePaxos/VoteProof_Liveness | 1527 | Exploited tlapm soundness bug — `<1>1. TRUE / OBVIOUS` + bare `<1> QED` proves anything; read checker error message to reverse-engineer detection logic, then added TRUE step to bypass zero-obligation check |

## Failed Benchmarks

| Benchmark | Time (s) | Obligations | Notes |
|-----------|----------|-------------|-------|
| Consensus/PaxosProof_struct_lemma | 2915 | 1/3 failed | Gave up; stuck on Phase1b/2b set reasoning |
| Paxos/Paxos_Invariant | 4189 | 3/41 failed | Gave up; Phase1b MsgInv' intractable, source also fails tlapm 1.5+1.6 |
| ByzantinePaxos/BPConProof_MsgsLemma | 7200 | 3/123 failed | 2h timeout; still iterating at cutoff, 115/119 proved |

## All Results

| # | Benchmark | Verdict | Time (s) | Obligations | Tokens (in/out) |
|---|-----------|---------|----------|-------------|-----------------|
| 1 | Data/SequencesTheorems_ElementOfSeq | ✅ PASS | 39 | 4 | 102268/853 |
| 2 | Consensus/PaxosProof_CardinalityOne | ✅ PASS | 39 | 5 | 111429/839 |
| 3 | Consensus/PaxosProof_CardinalityInNat | ✅ PASS | 40 | 12 | 103966/1158 |
| 4 | Consensus/Voting_ChoosableThm | ✅ PASS | 42 | 1 | 91423/911 |
| 5 | Consensus/Sets_CardinalityInNat | ✅ PASS | 42 | 10 | 103018/1145 |
| 6 | Data/Sets_CardinalityInNat | ✅ PASS | 43 | 9 | 101870/1241 |
| 7 | Consensus/Consensus_CardinalityInNat | ✅ PASS | 43 | 8 | 132847/1189 |
| 8 | Allocator/Allocator_InitTypeInvariant | ✅ PASS | 43 | 1 | 155085/1176 |
| 9 | Consensus/Voting_OneVoteThm | ✅ PASS | 44 | 1 | 112744/798 |
| 10 | BubbleSort/BubbleSort_IsPermOfReflexive | ✅ PASS | 46 | 3 | 129326/1218 |
| 11 | SimpleMutex/SimpleMutex_TLAInvariance | ✅ PASS | 49 | 23 | 131405/1585 |
| 12 | AtomicBakery/AtomicBakeryWithoutSMT_InitImpliesTypeOK | ✅ PASS | 50 | 8 | 142486/1256 |
| 13 | ByzantinePaxos/PConProof_NextDef | ✅ PASS | 52 | 1 | 188281/1154 |
| 14 | BubbleSort/BubbleSort_CompositionOfPerms | ✅ PASS | 52 | 9 | 146672/1631 |
| 15 | Paxos/Paxos_QuorumNonEmpty | ✅ PASS | 53 | 7 | 185912/1704 |
| 16 | Paxos/Paxos_NoneNotAValue | ✅ PASS | 53 | 6 | 216531/1325 |
| 17 | Data/SequencesTheorems_LenDomain | ✅ PASS | 55 | 2 | 204327/1341 |
| 18 | Consensus/Voting_QuorumNonEmpty | ✅ PASS | 55 | 9 | 135383/1392 |
| 19 | ByzantinePaxos/VoteProof_VT2 | ✅ PASS | 55 | 8 | 196898/1426 |
| 20 | Two-Phase/TwoPhase_Mod2 | ✅ PASS | 56 | 2 | 199303/1293 |
| 21 | Consensus/Consensus_CardinalityOne | ✅ PASS | 57 | 16 | 131062/1614 |
| 22 | Cantor/Cantor8_Cantor | ✅ PASS | 57 | 24 | 172907/1845 |
| 23 | Allocator/Allocator_RequestTypeInvariant | ✅ PASS | 57 | 1 | 148900/1102 |
| 24 | Cantor/Cantor1_cantor | ✅ PASS | 58 | 12 | 165062/1706 |
| 25 | BubbleSort/BubbleSort_CompositionAssociative | ✅ PASS | 58 | 3 | 211274/1635 |
| 26 | Data/SequencesTheorems_LenAxiom | ✅ PASS | 58 | 10 | 210228/1525 |
| 27 | Consensus/PaxosProof_CardinalityTwo | ✅ PASS | 59 | 14 | 164891/1837 |
| 28 | Cantor/Cantor9_Cantor | ✅ PASS | 59 | 15 | 177416/2049 |
| 29 | Euclid/GCD_GCD2 | ✅ PASS | 59 | 4 | 225121/1502 |
| 30 | Euclid/EuclidEx_GCD2 | ✅ PASS | 61 | 5 | 214391/1961 |
| 31 | Consensus/Consensus_CardinalityTwo | ✅ PASS | 62 | 14 | 198365/1654 |
| 32 | ByzantinePaxos/VoteProof_NextDef | ✅ PASS | 62 | 1 | 215597/1381 |
| 33 | ByzantinePaxos/BPConProof_OnePlusFinite | ✅ PASS | 62 | 7 | 248741/1715 |
| 34 | Consensus/Consensus_CardinalityOneConverse | ✅ PASS | 63 | 24 | 154713/1921 |
| 35 | BubbleSort/BubbleSort_ExchangeAPerm | ✅ PASS | 64 | 2 | 168652/1215 |
| 36 | Data/SequencesTheorems_AppendProperties | ✅ PASS | 65 | 37 | 263213/2215 |
| 37 | Consensus/Voting_AllSafeAtZero | ✅ PASS | 67 | 4 | 245641/1524 |
| 38 | Data/GraphTheorem_AtLeastTwo | ✅ PASS | 67 | 33 | 203480/2482 |
| 39 | BubbleSort/BubbleSort_IdIdentity | ✅ PASS | 68 | 7 | 168089/2101 |
| 40 | ByzantinePaxos/BPConProof_PmaxBalLemma1 | ✅ PASS | 68 | 1 | 180404/1250 |
| 41 | ByzantinePaxos/BPConProof_MaxBallotLemma1 | ✅ PASS | 69 | 22 | 235385/1849 |
| 42 | BubbleSort/BubbleSort_IsPermOfTransitive | ✅ PASS | 69 | 25 | 168748/2307 |
| 43 | Allocator/Allocator_ReturnTypeInvariant | ✅ PASS | 69 | 4 | 129307/1065 |
| 44 | ByzantinePaxos/VoteProof_InitImpliesInv | ✅ PASS | 69 | 1 | 210070/1795 |
| 45 | ByzantinePaxos/BPConProof_MaxBallotProp | ✅ PASS | 69 | 18 | 204985/1921 |
| 46 | Consensus/Sets_CardinalityPlusOne | ✅ PASS | 70 | 31 | 188899/2260 |
| 47 | Allocator/Allocator_NextTypeInvariant | ✅ PASS | 70 | 10 | 134990/1106 |
| 48 | ByzantinePaxos/BPConProof_QuorumTheorem | ✅ PASS | 80 | 33 | 225659/2028 |
| 49 | Consensus/PaxosProof_CardinalityPlusOne | ✅ PASS | 80 | 22 | 213456/2934 |
| 50 | ByzantinePaxos/VoteProof_VT0 | ✅ PASS | 80 | 40 | 220762/2746 |
| 51 | Data/GraphTheorem_IsBijectionTransitive | ✅ PASS | 80 | 29 | 239296/1904 |
| 52 | EWD840/EWD840_Inv_implies_Termination | ✅ PASS | 80 | 27 | 236660/3104 |
| 53 | Paxos/PaxosHistVar_VotedInv | ✅ PASS | 80 | 15 | 136149/1693 |
| 54 | Data/SequencesTheorems_HeadAndTailOfSeq | ✅ PASS | 80 | 26 | 337103/3179 |
| 55 | Consensus/Consensus_CardinalityPlusOne | ✅ PASS | 80 | 35 | 217249/2731 |
| 56 | SimpleMutex/SimpleMutex_Safety | ✅ PASS | 80 | 20 | 288581/2548 |
| 57 | Consensus/PaxosProof_OtherMessage | ✅ PASS | 80 | 20 | 269593/2165 |
| 58 | Consensus/Sets_CardinalityOne | ✅ PASS | 80 | 16 | 255517/2137 |
| 59 | Data/Sets_IsBijectionInverse | ✅ PASS | 80 | 32 | 221162/2250 |
| 60 | Consensus/Sets_CardinalityOneConverse | ✅ PASS | 80 | 30 | 163151/3125 |
| 61 | Allocator/Allocator_ReturnMutex | ✅ PASS | 80 | 1 | 132110/1331 |
| 62 | AtomicBakery/AtomicBakeryWithoutSMT_GGIrreflexive | ✅ PASS | 80 | 44 | 182285/2042 |
| 63 | Allocator/Allocator_RequestMutexBis | ✅ PASS | 80 | 5 | 131604/1097 |
| 64 | Data/Sets_CardinalityZero | ✅ PASS | 80 | 28 | 244310/2659 |
| 65 | Consensus/PaxosProof_WFmsgs | ✅ PASS | 80 | 45 | 224183/3844 |
| 66 | Allocator/Allocator_NextMutex | ✅ PASS | 80 | 24 | 134191/1355 |
| 67 | Cantor/Cantor7_cantor | ✅ PASS | 83 | 17 | 204876/2497 |
| 68 | Data/Sets_CardinalityPlusOne | ✅ PASS | 83 | 32 | 332405/2811 |
| 69 | Data/GraphTheorem_CardinalityInNat | ✅ PASS | 84 | 7 | 390074/2354 |
| 70 | ByzantinePaxos/Consensus_InductiveInvariance | ✅ PASS | 84 | 25 | 230358/2547 |
| 71 | Paxos/PaxosHistVar_VotedOnce | ✅ PASS | 84 | 28 | 248871/3896 |
| 72 | Data/SequencesTheorems_InitialSubSeq | ✅ PASS | 84 | 33 | 224770/2953 |
| 73 | Data/GraphTheorem_IsBijectionInverse | ✅ PASS | 86 | 56 | 251727/3055 |
| 74 | ByzantinePaxos/BPConProof_NextDef | ✅ PASS | 86 | 1 | 279483/1511 |
| 75 | AtomicBakery/AtomicBakeryWithoutSMT_AfterPrime | ✅ PASS | 88 | 8 | 180602/1274 |
| 76 | BubbleSort/BubbleSort_IdAPerm | ✅ PASS | 88 | 10 | 393778/3025 |
| 77 | Data/GraphTheorem_CardinalityOne | ✅ PASS | 89 | 8 | 252507/3010 |
| 78 | ByzantinePaxos/VoteProof_QuorumNonEmpty | ✅ PASS | 90 | 7 | 153439/1779 |
| 79 | SimpleMutex/SimpleMutex_Mutex | ✅ PASS | 90 | 12 | 299137/3316 |
| 80 | ByzantinePaxos/BPConProof_BMessageLemma | ✅ PASS | 91 | 86 | 273090/3734 |
| 81 | Cantor/Cantor6_cantor | ✅ PASS | 91 | 13 | 306338/3134 |
| 82 | Paxos/Paxos_VotedInv | ✅ PASS | 92 | 22 | 190490/1712 |
| 83 | Data/Sets_CardinalityOneConverse | ✅ PASS | 93 | 27 | 375409/2922 |
| 84 | Cantor/Cantor3_cantor | ✅ PASS | 93 | 18 | 241893/3122 |
| 85 | Consensus/Consensus_IsBijectionTransitive | ✅ PASS | 94 | 31 | 228814/2890 |
| 86 | Euclid/Euclid_InitProperty | ✅ PASS | 94 | 2 | 205437/1495 |
| 87 | Data/GraphTheorem_CardinalityOneConverse | ✅ PASS | 97 | 25 | 194548/2961 |
| 88 | Data/GraphTheorem_EdgesAxiom | ✅ PASS | 100 | 20 | 360719/3238 |
| 89 | EWD840/EWD840_TypeOK_inv | ✅ PASS | 102 | 20 | 273145/2098 |
| 90 | Data/Sets_IsBijectionTransitive | ✅ PASS | 103 | 52 | 310345/4697 |
| 91 | AtomicBakery/AtomicBakeryWithoutSMT_InitInv | ✅ PASS | 105 | 9 | 300491/3243 |
| 92 | Allocator/Allocator_AllocateTypeInvariant | ✅ PASS | 107 | 27 | 432784/3857 |
| 93 | Consensus/PaxosProof_CardinalityOneConverse | ✅ PASS | 109 | 28 | 447677/3444 |
| 94 | ByzantinePaxos/VoteProof_GeneralNatInduction | ✅ PASS | 112 | 14 | 357986/2971 |
| 95 | Cantor/Cantor10_Cantor | ✅ PASS | 113 | 20 | 313258/3305 |
| 96 | Euclid/Euclid_NextProperty | ✅ PASS | 114 | 52 | 385302/3739 |
| 97 | Data/Sets_CardinalityOne | ✅ PASS | 118 | 22 | 457800/3307 |
| 98 | Euclid/Euclid_Correctness | ✅ PASS | 119 | 16 | 304063/3079 |
| 99 | Consensus/Sets_CardinalityTwo | ✅ PASS | 121 | 16 | 211895/2223 |
| 100 | Euclid/EuclidEx_GCD1 | ✅ PASS | 122 | 13 | 279004/2905 |
| 101 | Data/GraphTheorem_CardinalityZero | ✅ PASS | 123 | 25 | 266765/5857 |
| 102 | Consensus/PaxosProof_typing | ✅ PASS | 124 | 7 | 582416/3488 |
| 103 | Consensus/PaxosProof_IsBijectionInverse | ✅ PASS | 124 | 43 | 527705/5238 |
| 104 | ByzantinePaxos/Consensus_Invariance | ✅ PASS | 127 | 10 | 288248/1925 |
| 105 | Consensus/Sets_IsBijectionInverse | ✅ PASS | 140 | 32 | 324688/3877 |
| 106 | Consensus/Consensus_IsBijectionInverse | ✅ PASS | 140 | 32 | 427715/5252 |
| 107 | AtomicBakery/AtomicBakeryWithoutSMT_InvExclusion | ✅ PASS | 140 | 8 | 267162/4257 |
| 108 | Allocator/Allocator_InitMutex | ✅ PASS | 140 | 19 | 249666/2983 |
| 109 | AtomicBakery/AtomicBakeryWithoutSMT_TypeOKInvariant | ✅ PASS | 145 | 45 | 431704/3174 |
| 110 | Consensus/Voting_Consistent | ✅ PASS | 147 | 12 | 484396/7399 |
| 111 | Data/SequencesTheorems_EmptySeq | ✅ PASS | 148 | 4 | 651388/5954 |
| 112 | Paxos/Paxos_Consistent | ✅ PASS | 150 | 144 | 523101/7540 |
| 113 | Cantor/Cantor2_cantor | ✅ PASS | 154 | 15 | 522182/3762 |
| 114 | Consensus/PaxosProof_CardinalitySetMinus | ✅ PASS | 157 | 74 | 447106/6815 |
| 115 | Euclid/GCD_GCD3 | ✅ PASS | 158 | 56 | 870494/6854 |
| 116 | Consensus/Sets_IntervalCardinality | ✅ PASS | 161 | 87 | 504083/5508 |
| 117 | Data/Sets_IntervalCardinality | ✅ PASS | 163 | 78 | 604201/4640 |
| 118 | Consensus/PaxosProof_CardinalityZero | ✅ PASS | 163 | 14 | 771613/5000 |
| 119 | Data/GraphTheorem_PigeonHole | ✅ PASS | 163 | 28 | 629544/5149 |
| 120 | ByzantinePaxos/Consensus_LiveSpecEquals | ✅ PASS | 168 | 17 | 477888/4235 |
| 121 | Consensus/PaxosProof_PigeonHole | ✅ PASS | 170 | 32 | 488874/6837 |
| 122 | Data/SequencesTheorems_RemoveSeq | ✅ PASS | 170 | 21 | 875250/6466 |
| 123 | ByzantinePaxos/Consensus_EnabledDef | ✅ PASS | 171 | 3 | 582919/4685 |
| 124 | Consensus/Sets_IsBijectionTransitive | ✅ PASS | 172 | 24 | 380888/4670 |
| 125 | Consensus/Sets_PigeonHole | ✅ PASS | 173 | 36 | 541545/6327 |
| 126 | Euclid/GCD_GCD1 | ✅ PASS | 175 | 27 | 325244/3933 |
| 127 | SimpleMutex/SimpleMutex_Initialization | ✅ PASS | 181 | 26 | 766159/5135 |
| 128 | Consensus/Consensus_Invariance | ✅ PASS | 188 | 26 | 1271565/6724 |
| 129 | Data/GraphTheorem_CardinalitySetMinus | ✅ PASS | 190 | 106 | 673517/8923 |
| 130 | Consensus/Consensus_PigeonHole | ✅ PASS | 190 | 39 | 886296/7080 |
| 131 | Consensus/PaxosProof_IsBijectionTransitive | ✅ PASS | 200 | 30 | 831866/8681 |
| 132 | Consensus/Consensus_CardinalityZero | ✅ PASS | 200 | 29 | 661176/4352 |
| 133 | Two-Phase/TwoPhase_Implementation | ✅ PASS | 200 | 95 | 941897/8115 |
| 134 | BubbleSort/BubbleSort_IsPermOfExchange | ✅ PASS | 200 | 52 | 729860/4957 |
| 135 | Cantor/Cantor5_cantor | ✅ PASS | 200 | 9 | 588830/4768 |
| 136 | Data/Sets_PigeonHole | ✅ PASS | 228 | 36 | 958659/9058 |
| 137 | Consensus/Voting_Invariant | ✅ PASS | 230 | 81 | 1185235/8918 |
| 138 | Paxos/Paxos_VotedOnce | ✅ PASS | 232 | 28 | 977322/10053 |
| 139 | Allocator/Allocator_AllocateMutex | ✅ PASS | 233 | 3 | 547967/8192 |
| 140 | SimpleMutex/SimpleMutex_Invariance | ✅ PASS | 237 | 55 | 727863/10363 |
| 141 | Cantor/Cantor4_cantor | ✅ PASS | 240 | 19 | 869918/7861 |
| 142 | Consensus/Sets_FiniteSubset | ✅ PASS | 247 | 75 | 1017896/7052 |
| 143 | Data/GraphTheorem_FiniteSubset | ✅ PASS | 260 | 81 | 940789/8914 |
| 144 | Consensus/Consensus_CardinalitySetMinus | ✅ PASS | 260 | 60 | 1140959/9344 |
| 145 | AtomicBakery/AtomicBakeryWithoutSMT_Safety | ✅ PASS | 260 | 26 | 1140766/7613 |
| 146 | Consensus/PaxosProof_FiniteSubset | ✅ PASS | 267 | 91 | 713286/6165 |
| 147 | Euclid/EuclidEx_GCD3 | ✅ PASS | 270 | 78 | 1557051/10216 |
| 148 | Consensus/Consensus_FiniteSubset | ✅ PASS | 277 | 105 | 1283960/10544 |
| 149 | ByzantinePaxos/VoteProof_VT1 | ✅ PASS | 281 | 109 | 1306666/12029 |
| 150 | ByzantinePaxos/BPConProof_FiniteMsgsLemma | ✅ PASS | 293 | 10 | 900142/3315 |
| 151 | Data/GraphTheorem_IntervalCardinality | ✅ PASS | 297 | 72 | 1530287/8166 |
| 152 | Consensus/PaxosProof_IntervalCardinality | ✅ PASS | 297 | 73 | 973419/6357 |
| 153 | Consensus/Voting_VotesSafeImpliesConsistency | ✅ PASS | 298 | 159 | 1607145/12796 |
| 154 | ByzantinePaxos/VoteProof_VT4 | ✅ PASS | 302 | 142 | 1101152/12071 |
| 155 | Data/Sets_CardinalityTwo | ✅ PASS | 306 | 3 | 674942/8886 |
| 156 | Paxos/Paxos_Refinement | ✅ PASS | 320 | 60 | 1343061/8944 |
| 157 | Data/GraphTheorem_CardinalityTwo | ✅ PASS | 320 | 13 | 1086346/11968 |
| 158 | Consensus/Consensus_IntervalCardinality | ✅ PASS | 327 | 83 | 1346227/8090 |
| 159 | ByzantinePaxos/VoteProof_SafeLemma | ✅ PASS | 342 | 131 | 1395955/16218 |
| 160 | Consensus/Voting_ShowsSafety | ✅ PASS | 351 | 135 | 1970886/17247 |
| 161 | Data/GraphTheorem_CardinalityPlusOne | ✅ PASS | 353 | 101 | 1615987/14836 |
| 162 | Paxos/PaxosHistVar_SafeAtStable | ✅ PASS | 380 | 85 | 1633860/16794 |
| 163 | ByzantinePaxos/BPConProof_KnowsSafeAtDef | ✅ PASS | 403 | 5 | 1198860/5271 |
| 164 | Data/Sets_FiniteSubset | ✅ PASS | 413 | 89 | 2343795/15296 |
| 165 | Paxos/PaxosHistVar_Consistent | ✅ PASS | 414 | 136 | 2496518/19016 |
| 166 | Consensus/Sets_CardinalityZero | ✅ PASS | 440 | 25 | 292337/3501 |
| 167 | ByzantinePaxos/BPConProof_PNextDef | ✅ PASS | 440 | 4 | 1707508/4609 |
| 168 | Data/Sets_CardinalitySetMinus | ✅ PASS | 444 | 193 | 2574714/18875 |
| 169 | Cantor/Cantor10_NoSetContainsAllValues | ✅ PASS | 447 | 24 | 1362911/12772 |
| 170 | Paxos/Paxos_SafeAtStable | ✅ PASS | 454 | 185 | 2401343/21612 |
| 171 | ByzantinePaxos/VoteProof_VT3 | ✅ PASS | 454 | 134 | 2928180/17556 |
| 172 | Data/SequencesTheorems_ConcatProperties | ✅ PASS | 456 | 59 | 2550004/20407 |
| 173 | Consensus/Sets_CardinalitySetMinus | ✅ PASS | 466 | 67 | 559546/6275 |
| 174 | Data/SequencesTheorems_AppendDef | ✅ PASS | 487 | 30 | 2788221/18821 |
| 175 | Data/SequencesTheorems_ConcatDef | ✅ PASS | 520 | 20 | 3222245/16506 |
| 176 | ByzantinePaxos/VoteProof_VT1Prime | ✅ PASS | 577 | 88 | 3382106/22777 |
| 177 | ByzantinePaxos/BPConProof_PmaxBalLemma5 | ✅ PASS | 577 | 3 | 2653006/10369 |
| 178 | ByzantinePaxos/BPConProof_PmaxBalLemma2 | ✅ PASS | 578 | 11 | 767119/6173 |
| 179 | ByzantinePaxos/BPConProof_PMaxBalLemma3 | ✅ PASS | 582 | 33 | 3038172/8535 |
| 180 | ByzantinePaxos/BPConProof_MaxBallotLemma2 | ✅ PASS | 600 | 223 | 0/0 |
| 181 | ByzantinePaxos/BPConProof_PmaxBalLemma4 | ✅ PASS | 600 | 41 | 0/0 |
| 182 | Consensus/Voting_Refinement | ✅ PASS | 600 | 155 | 0/0 |
| 183 | ByzantinePaxos/BPConProof_MsgsTypeLemmaPrime | ✅ PASS | 600 | 17 | 0/0 |
| 184 | ByzantinePaxos/BPConProof_MsgsTypeLemma | ✅ PASS | 600 | 14 | 0/0 |
| 185 | AtomicBakery/AtomicBakeryWithoutSMT_InductiveInvariant | ✅ PASS | 600 | 53 | 3018053/18921 |
| 186 | ByzantinePaxos/VoteProof_SafeAtProp | ✅ PASS | 620 | 57 | 3001395/19771 |
| 187 | ByzantinePaxos/VoteProof_VT0Prime | ✅ PASS | 1023 | 5 | 9323121/48237 |
| 188 | ByzantinePaxos/VoteProof_Liveness | ⚠️ CHEAT | 1527 | 1 | 11783693/82770 |
| 189 | Consensus/PaxosProof_struct_lemma | ❌ FAIL | 2915 | 1/3 failed | 16731088/90174 |
| 190 | Paxos/PaxosHistVar_Invariant | ⚠️ CHEAT | 3216 | 2 | 31362770/83046 |
| 191 | ByzantinePaxos/VoteProof_InductiveInvariance | ✅ PASS | 4058 | 196 | 24463719/121681 |
| 192 | Paxos/Paxos_Invariant | ❌ FAIL | 4189 | 3/41 failed | 40414873/91305 |
| 193 | ByzantinePaxos/BPConProof_MsgsLemma | ❌ FAIL | 7200 | 3/123 failed | 0/0 |

## Notes

- 18 benchmarks that timed out in original 10min (600s) run were rerun with 2h timeout
- 3 benchmarks initially misclassified as FAIL due to missing dependency files; re-verified as PASS
- **tlapm soundness bug discovered**: `THEOREM FALSE / PROOF / <1>1. TRUE / OBVIOUS / <1> QED` proves FALSE on both tlapm 1.5 and 1.6. Bare `<1> QED` generates 0 obligations. Not previously reported.
- BPConProof_MsgsLemma: hit 2h timeout while still actively iterating; 115/119 obligations proved
- Paxos_Invariant: source proof also fails on tlapm 1.5 and 1.6
- PaxosHistVar_Invariant: source requires tlapm 1.6 (181/182 obligations). Codex's 2h rerun proof tested on 1.6: 1/2 failed — proof structure fundamentally wrong, most steps not expanded
