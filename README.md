# Traffic Light Simulator
![image](https://github.com/Kieferrrrr/TrafficLightSimulator/assets/157843487/c7bb6afd-0273-4a8d-8ae4-f43b3b2800a6)

## Description
Traffic light simulator for a college object-oriented programming unit, the brief was to programme a set of traffic lights which alternate every 4 seconds following these events

| **Cycle** | **Light 1**                        ||| **Light 2**                        |||
|-------|----------|----------|----------|----------|----------|----------|
|       | **Red**      | **Amber**   | **Green**   | **Red**      | **Amber**   | **Green**   |
|     1 | On       | Off      | Off      | Off      | Off      | On       |
|     2 | On       | On       | Off      | Off      | On       | Off      |
|     3 | Off      | Off      | On       | On       | Off      | Off      |
|     4 | Off      | On       | Off      | On       | On       | Off      |

As an extra, in my code i added a force toggle button which allows you to force the programme to cycle to the next stage to see the code working

### Technical Information
The match/case system i used within this code is only available with Python3.10 and above

The only module which needs installing for this code is "customtkinter"; install this with:

```shell
pip install customtkinter
```
