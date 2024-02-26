Implementation of "iFair: Learning individually Fair Data Representations for Algorithmic Decision Making"

Summary :

According to the paper, we tried to implement a method for probabilistically mapping user records into a low-rank representation that reconciles individual fairness and the utility of classifiers and rankings in downstream applications.
Focus on "Individual Fairness" because "Individual Fairness" carefully traded off with "Utility" of Classifiers & Ranking observed to perform much better.

Packages Required & Version :
 
| S.No |   Package Name  |     Version   |
|------|-----------------|---------------|
|      |                 |               |
| 1.   |     scipy       |      1.4.1    |
| 2.   |    sklearn      |      0.0      |
| 3.   |     numpy       |      1.18.3   |
| 4.   |    pandas       |      1.0.3    |
| 5.   |      csv        |               |
| 6.   |     math        |               |

Python Version - 3.8 (Python Interpreter - 3.8.2)

Results :

| S.No  |       Attributes        |        Original Dataset (Code) |      iFair Transformed Dataset(Paper)     |  iFair Transformed Dataset(Code)  |
|-------|-------------------------|--------------------------------|-------------------|----------------|
|       |                         |                                |                   |                |
| 1.    |        Accuracy         |             0.7413             |       0.78        |    0.769       |
| 2.    |    Individual Fairness  |             0.831              |       0.92        |    0.902       |

Uncompleted Tasks / issues  :
1. We were unable to get the Utility measure for the evaluation part(as of now) as the process for it seems tedious.
2. We were able to work on Ranking Datasets as the Input Datasets for those needs lots of Preprocessing which were not mentioned in the paper even.

Todo :
1. Will be trying to find out Preprocessing measures for the Ranking Datasets and try to make the code work for those datasets too.

Team Members :

| S.No |       Name               |    Roll No    |
|------|--------------------------|---------------|
|      |                          |               |
| 1.   |    Manoj Preveen         |    15MA20023  |
| 2.   |    Shayan Shafquat       |    15MA20038  |
| 3.   |    Krishnakant Deshmukh  |    15EE32001  |
| 4.   |    Manad Mishra          |    16CS30019  |

