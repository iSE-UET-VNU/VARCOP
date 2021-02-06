## Variability Fault Localization

Software fault localization is one of the most expensive, tedious, and time-consuming activities in program debugging. This activity becomes even much more challenging in Software Product Line (SPL) systems due to the variability of failures in SPL systems. These unexpected behaviors are caused by variability faults which can only be exposed under some combinations of system features because of the interaction among these features. In this article, we present VarCop, a novel and effective variability fault localization approach. For an SPL system failed by variability bugs, VarCop isolates suspicious code statements by analyzing the test results and source code of the tested products. The suspicious statements are the statements related to the interaction among the features which potentially make the bugs (in)visible in the products. After that, VarCop ranks the isolated suspicious statements by considering their suspiciousness levels measured in the failing products, as well as, their contributions in the passing products. On a large dataset of buggy SPL systems, our empirical evaluation shows that VarCop significantly improved the state-of-the-art fault localization technique by 47% and 39% in Rank and EXAM, respectively. For the systems containing a single variability bug, in +60% of the cases, VarCop correctly ranks the buggy statements at the top-3 positions in the resulting lists. In the cases of multiple bugs, VarCop also outperforms the state-of-the-art approach more than three times in the proportion of the bugs localized at the top-1 positions. On average, it correctly localizes 21% and 50% of the bugs in a system at the top-1 and top-5 positions respectively. Especially, in +50% of the buggy versions, VarCop effectively ranks at least one buggy statement first in the resulting lists. Moreover, in these lists, one or more bugs in +90% of the cases are correctly localizes at the top-3 positions.

### Empirical results
1. Performance Comparison
    1. VarCop's performance compared to the state-of-the-art approaches 
        1. [By Rank and EXAM](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/PERFORMANCE%20COMPARISON/Performance_comparison.xlsx)
        2. [By Hit@X](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/PERFORMANCE%20COMPARISON/Hit%40x.xlsx)
    1. [VarCop's performance by Mutation Operators causing bugs](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/PERFORMANCE%20COMPARISON/performance_comparison_by_mutation_operators.xlsx)
    1. [VarCop's performance by bugs' code elements](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/PERFORMANCE%20COMPARISON/performance_comparison_by_code_elements.xlsx)
    1. [VarCop's performance by the number of involving features](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/PERFORMANCE%20COMPARISON/performance_comparison_by_Num_of_involving_features.xlsx)
1. Intrinsic Analysis
    1. [Impact of Suspicious Statement Isolation on performance](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/INTRINSIC%20ANALYSIS/Impact%20Suspicious%20Statement%20Isolation.xlsx)
    1. [Impact of choosing Metric of Local Suspiciousness Measurement on performance](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/PERFORMANCE%20COMPARISON/Performance_comparison.xlsx)
    1. [Impact of Normalization on performance](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/INTRINSIC%20ANALYSIS/Impact%20of%20Normalization.xlsx)
    1. [Impact of choosing Aggreation Function of Global Suspiciousness Measurement on performance](https://github.com/ttrangnguyen/VARCOP/blob/gh-pages/INTRINSIC%20ANALYSIS/Impact%20of%20Aggregation%20function.xlsx)
1. Sensitivity Analysis
    1. [Impact of Sample Size on performance](https://github.com/ttrangnguyen/VARCOP/tree/gh-pages/SENSITIVITY%20ANALYSIS/Impact%20of%20sample%20size)
    1. [Impact of Test Suite's Size on performance](https://github.com/ttrangnguyen/VARCOP/tree/gh-pages/SENSITIVITY%20ANALYSIS/Impact%20of%20test%20suite's%20size)
1. [Performance In Localizing Multiple Bugs](https://github.com/ttrangnguyen/VARCOP/tree/gh-pages/MULTIPLE%20BUGS)
1. [Time Complexity](https://github.com/ttrangnguyen/VARCOP/tree/gh-pages/RUNTIME)

### Dataset
1. GPL
    1. [Source code](https://drive.google.com/file/d/1YjxWuqxi8A6luNeSKV0qcTD_sY4zpPee/view?usp=sharing)
    1. [Bugs](https://drive.google.com/drive/folders/1Esp1935opTL2ZTnXFo3HW9eRaROP6zGV?usp=sharing)
    1. [Experimental results](https://github.com/ttrangnguyen/VARCOP/tree/gh-pages/DETAIL/GPL)
1. Zipme
    1. [Source code](https://drive.google.com/file/d/1ygoxcVyXNpD4DGebWJRDHvYc4h0cqM25/view?usp=sharing)
    1. [Bugs](https://drive.google.com/drive/folders/15RcMIOsHct94gO67aCVBH_f5Sj788zrp?usp=sharing)
    1. [Experimental results](https://github.com/ttrangnguyen/VARCOP/tree/gh-pages/DETAIL/ZipMe)
1. Email
    1. [Source code](https://drive.google.com/file/d/1fubwYmhx-s9SUwcsc_KKKlg0YxcN8Wdx/view?usp=sharing)
    1. [Bugs](https://drive.google.com/drive/folders/1zkijJVR4Abtb7r6Qt_sEUA1hzpJ7cUoC?usp=sharing)
    1. [Experimental results](https://github.com/ttrangnguyen/VARCOP/tree/gh-pages/DETAIL/Email)
1. ExamDB
    1. [Source code](https://drive.google.com/file/d/1szj3mWJe7vInYpNclJ54BBZkDc1mF_kK/view?usp=sharing)
    1. [Bugs](https://drive.google.com/drive/folders/1n-RpR0y5rf0pBsHSQV4htkB5KEHmwbbL?usp=sharing)
    1. [Experimental results](https://github.com/ttrangnguyen/VARCOP/tree/gh-pages/DETAIL/ExamDB)
1. BankAccountTP
    1. [Source code](https://drive.google.com/file/d/1D-BXOD5xCiLVPDELtf4yQmJV9nF4GuN7/view?usp=sharing)
    1. [Bugs](https://drive.google.com/drive/folders/1iGEsEgelgwjfQQES5VYUiI49242Pirtp?usp=sharing)
    1. [Experimental results](https://github.com/ttrangnguyen/VARCOP/tree/gh-pages/DETAIL/BankAccountTP)
1. Elevator
    1. [Source code](https://drive.google.com/file/d/1IdyJrcA-GGdapNIEf6POByUQPyifBW6E/view?usp=sharing)
    1. [Bugs](https://drive.google.com/drive/folders/1Esp1935opTL2ZTnXFo3HW9eRaROP6zGV?usp=sharing)
    1. [Experimental results](https://github.com/ttrangnguyen/VARCOP/tree/gh-pages/DETAIL/Elevator)
