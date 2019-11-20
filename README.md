# A Software Architecture for Multimodal Semantic Perception Fusion

## Objective of the Project
The prject proposes an implementation of architecture to fuse geometric features computed from point clouds and Convolution Neural Network (CNN) classifications, based on images.

## The System’s Architecture

### Overall Architecture
It describes what the project wants to achieve and defines the key terminologies of this project. Presents the hardware or tools used in the project.

<p align="center"> 
<img src="https://github.com/maicivan/sofar_multimodal/blob/master/imgs/Schermata%202019-11-14%20alle%2014.55.55.png">
</p>

#### Messages
##### Feature.msg

```
string types
string name
string[] value
```
##### Obj.msg

```
feature[] obj
```
##### Adapter.msg

```
uint32 id_mod
obj[] adap
```
##### CommonFeature.msg

```
adapter[] common
```
##### FeatureMatcher.msg

```
commonFeature[] matcher
```
##### Corr.msg

```
string first_percepted_object
string second_percepted_object
float32 correlation
```
##### CorrelationTable.msg

```
corr[] table
```
##### Record.msg

```
string[] rec
float32 corr
```
##### OutputReasoner.msg

```
record[] lines
```
##### MatcherObj.msg

```
obj[] sameObj
float32 correlation
```
### Description of the Modules
#### PITT Perception module
It describes all the modules within the architecture, i.e, (i) the inputs, (ii) the internal working, and (iii) the outputs.
* __Input__: 
* __Output__:
* __Publisher__: [__O1__]

#### Tensorflow Perception module
It describes all the modules within the architecture, i.e, (i) the inputs, (ii) the internal working, and (iii) the outputs.
* __Input__: 
* __Output__:
* __Publisher__: [__O2__]

#### Adapter module
It's a module between a perception module and Feature selector module and makes a standard message for each perception module.  We provide an adapter for the Pitt module and another for the Tensorflow module. 
To add another perception module, it needs to implement a different adapter.
* __Input__: a type of message of a perception module
* __Output__: an adapter.msg
* __Publisher__: /outputAdapterPitt | /outputAdapterTensor

#### Features Selector module
It describes all the modules within the architecture, i.e, (i) the inputs, (ii) the internal working, and (iii) the outputs.
* __Input__: an adapter.msg
* __Output__: a selectorMatcher.msg
* __Publisher__: /featureScheduler/pubIntersection [__F__]| /featureScheduler/pubUnion [__R__]

#### Features Matcher module
It describes all the modules within the architecture, i.e, (i) the inputs, (ii) the internal working, and (iii) the outputs.
* __Input__: a selectorMatcher.msg | outputReasoner.msg
* __Output__: a matcherObj.msg
* __Publisher__: /featureMatcher/dataPub [__P__]

#### Table matcher module
It describes all the modules within the architecture, i.e, (i) the inputs, (ii) the internal working, and (iii) the outputs.
* __Input__: 
* __Output__:
* __Publisher__: [__T__]

#### Reasoner module
It describes all the modules within the architecture, i.e, (i) the inputs, (ii) the internal working, and (iii) the outputs.
* __Input__: 
* __Output__:
* __Publisher__: [__U__]

## Implementation

### Prerequisites
It describes all hardwares and softwares that are required for running the system.

### How to run the project
It describes step by step how to download and run the project on a new computer.

## Results
It presents the result using (images or videos) of the working system, in (real or simulation).

## Recommendations
The Recommendations follow naturally from the conclusions. They describe: the assumptions made while building the system (and/or) the limitations of the working system. Therefore, presenting possible ideas that could overcome the limitations or assumptions. 

## Authors
* Filippo Lapide
* Vittoriofranco Vagge

# Useful GitHub readme syntax

## To make bullet points

* Do this
	* Do this

## To make hyper-link

For example, making a link to [ROS tutorials](http://wiki.ros.org/ROS/Tutorials)

## To show, how to execute some commands in the terminal

    ```
    sudo apt install ros-kinetic-opencv3 #(should be already installed with previous point)
    sudo apt install ros-kinetic-opencv-apps
    ```

## To exphasize about a particular command

For example: Please do a ```catkin_make```, once you have modified your code. 

## To add image(s) or video(s)


* To link a [video](https://youtu.be/-yOZEiHLuVU)

## Reference
[Concept guide.](https://guides.github.com/features/wikis/)
[Syntax guide.](https://help.github.com/en/articles/basic-writing-and-formatting-syntax)
