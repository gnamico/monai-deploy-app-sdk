### Introduction
Productionizing an AI model is difficult as there is a chasm between training an AI model and deploying it to a production environment. In the healthcare domain, this chasm involves more than just performing inference with a model. An App developer would need to address issues such as: ingestion of medical imaging datasets, performing application specific pre and post processing operations,  packaging output from the application, integration with clinical informatics systems & ensuring right compute resources are specified and utilized by the application at run-time 

The MONAI Application SDK provides a framework to develop, verify, analyze AI driven healthcare applications and integrate them with clinical information systems using industry standard protocols such as DICOM & FHIR. The SDK is aimed to support the following activities

* Pythonic Framework for app development
* A mechanism to locally run and test an app
* A lightweight app analytics module
* A lightweight 2D/3D visualization module
* A developer console that provides a visual interface to all assets needed for developing apps
* A set of sample applications
* API documentation & User's Guide

---

### Scope

The scope of this document is limited to the MONAI Deploy App SDK. There are other subsystems of the MONAI Deploy platform such as MONAI App Server, MONAI App Informatics Gateway. However this requirements document does not address specifications belonging to those subsystems

---


### Attributes of a Requirement

For each requirements, the following attributes have been spcified
* Requirement Body: This is the text of the requirement which describes the goal and purpose behind the requirement
* Background: Provides necessary background to understand the context of the requirements
* Verficiation Strategy: A high level plan on how to test this requirement at a system level
* Target Release: Specifies which release of the MONAI App SDK this requirement is targeted for

---




### [REQ] Representing application specific tasks using Operators
The SDK shall enable representing a computational task in a healthcare application using an operator so that each task can be modulrized, reused and dubugged in distinct contexts.

#### Background
Most healthcare application workflows involves multiple tasks. Each task is a basic unit of work. Having a programmatic way of representing such task is important as this promotes separation of concern, reusability and debuggability. Example of tasks are: loading a DICOM Series into an in-memory volumetric representation, ability to rescale a volumetric etc.

#### Verification Strategy
Verify that common set of workflow tasks can be represented by built-in Operators

#### Target Release
MONAI Deploy App SDK 0.1.0

---



### [REQ] Inputs for Operators
The SDK shall provide mechanisms so that each Operator can be designed to ingest one or more inputs. 


#### Background
Often an application task requires to input multiple inputs. Having built-in support to model this behavior makes app development easier.

#### Verification Strategy
Verify that there is built-in support for multiple inputs for designing an operator


#### Target Release
MONAI Deploy App SDK 0.1.0

---




### [REQ] Outputs for Operators
The SDK shall provide mechanisms so that each Operator can be designed to generate one or more outputs. 


#### Background
Often an application task requires to generate multiple outpus. Having built-in support to model this behavior makes app development easier.

#### Verification Strategy
Verify that there is built-in support for multiple outputs for designing an operator


#### Target Release
MONAI Deploy App SDK 0.1.0

---



### [REQ] Representing Workflow With DAG
The SDK shall enable dependencies among upstream and downstream operators in an application using a DAG so that app workflow can be modeled unambiguously. The SDK shall provide a mechanism to link an output port of an upstream operator to an input port of a downstream operator to form the DAG

#### Background
Most healthcare application workflows involves multiple stages. Application developers need a way to organize functional units of AI based inference apps. A DAG (Directed Acyclic Graph) is the core concept of MONAI App SDK, collecting Operators together, organized with dependencies and relationships to specify how they should run.

#### Verification Strategy
Build an application with the SDK which has multiple operators. Verify that the SDK offers a mechanism to represent the underlying worklfow using a DAG and enables traversal of the DAG

#### Target Release
MONAI Deploy App SDK 0.1.0

---

### [REQ] Representing Workflow with DCG
The SDK shall enable representation of application workflows using a Directed Cyclic Graph (DCG) which requires cyclic dependencies

#### Background
Some applications require cycles to have dependencies among operators to represent application workflow.

#### Verification Strategy
Pick an application workflow from Genomics type which requires cyclic dependencies among operators. Verify that the App SDK supports such need.

#### Target Release
MONAI Deploy App SDK 0.2.0

----



### [REQ]  Conditional Branching in Workflow
The SDK shall support dynamic activation of an Operator in an application so that at run-time an Operator can be executed depending on application specific logic.

#### Background
Some applications require coniditional selection of an operator during run-time. Consider an application the following operators: (a) DICOM Data Loader (b) Rescale (c) Gaussin Blur (d) Classification Inference (e) DICOM Segmentation Writer. The app developer may select Rescale or Gaussian Blur operator depending on whether the input volumetric data requires rescaling or not.

#### Verification Strategy
Verify that operators can be dynamically selected for execution based on user specified logic

#### Target Release
MONAI Deploy App SDK 0.2.0

---


### [REQ]  Supporting logging for an Operator
The SDK shall support logging data from an Operator in a standardized way which can be parsed to aid in app debugging purpose

#### Background
A significant portion of app development in the healthcare AI domain is spent in figuring out anomalies in the core business logic of the application. Having a standardized way to log data will make it easier to debug the application


#### Verification Strategy
Use the SDK to log data from an operator. Verify that the logged data is adhereing to the logging schema


#### Target Release
MONAI Deploy App SDK 0.2.0

---



### [REQ]  Developing custom Operator
The SDK shall support developing custom Operators to perform task specific logic so that application developer is not limited by the built-in operators offered by the SDK itself


#### Background
The SDK itself will provide a set of built-in operators which can be incorporated domain specific tasks such as loading medical images, performing inference etc. However in almost all non-trivial applications, there would be need of performing custom tasks.


#### Verification Strategy
Write a custom operator to perform an image processing task and integrate that with an application using the App SDK.


#### Target Release
MONAI Deploy App SDK 0.1.0

---


### [REQ]  Support for Multi-Class Single-Output Classification
The SDK shall support developing an application that performs Multi-Class Single-Outout Classification classification with a pre-trained AI model so that the app developer can incorporate necessary model inputs, transforms, inference and package output from inference in appropriate domain-specific manners.

#### Background
Multiclass classification is a classification task with two or more classes. Each sample can only be labeled as one class. For example, classification using features extracted from a set of slices of different modalities, where each slice may either MR, CT or IVUS. Each image is one sample and is labeled as one of the 3 possible classes. Multiclass classification makes the assumption that each sample is assigned to one and only one label - one sample cannot, for example, be both a CT & MR.

#### Verification Strategy

Use a pre-trained model designed for multi-class classification. Verify that the SDK provides built-in operators using which an app can be built with that pre-trained model 


#### Target Release
MONAI Deploy App SDK 0.1.0

---



### [REQ]  Support for Multi-Class Multi-Output Classification
The SDK shall support developing an application that performs Multi-Class Multi-Output classification with a pre-trained AI model so that the app developer can incorporate necessary model inputs, transforms, inference and package output from inference in appropriate domain-specific manners.

#### Background
Multiclass-multioutput classification (also known as multitask classification) is a classification task which labels each sample with a set of non-binary properties. Both the number of properties and the number of classes per property is greater than 2. An example would be classifying a Chest X-Ray image to have one or more labels from the following list: Atelectasis, Cardiomegaly, Effusion, Pneumothorax  


#### Verification Strategy
Use a pre-trained model designed for multi-class multi-output classification. Verify that the SDK provides built-in operators using which an app can be built with that pre-trained model 


#### Target Release
MONAI Deploy App SDK 0.1.0

---



### [REQ]  Support for Semantic Segmentation
The SDK shall support developing an application that performs semantic segmentation with a pre-trained AI model so that the app developer can incorporate necessary model inputs, transforms, inference and package output from inference in appropriate domain-specific manners.

#### Background
The aim of semantic segmentation is to label each voxel in an image with a class. An example would to be assign each voxel in a 3D CT dataset to background, kidney or tumor.

#### Verification Strategy
Use a pre-trained model designed for semantic segmentation. Verify that the SDK provides built-in operators using which an app can be built with that pre-trained model 


#### Target Release
MONAI Deploy App SDK 0.1.0

---


### [REQ]  Support for Instance Segmentation
The SDK shall support developing an application that performs semantic segmentation with a pre-trained AI model so that the app developer can incorporate necessary model inputs, transforms, inference and package output from inference in appropriate domain-specific manners.


#### Background
In instance segmentation a model assigns an “individual object” label to each voxel in the image. An example would be where voxels for individual Lung nodues are labeled seperately. Let's say in a 3D dataset there are 20 lung nodules. Instead of having a generic "nodule" pixel class, we would have 20 classes for the 20 nodules: nodule-1, nodule-2, nodule-3,.., nodule-20.


#### Verification Strategy
Use a pre-trained model designed for Instance Segmentation. Verify that the SDK provides built-in operators using which an app can be built with that pre-trained model 


#### Target Release
MONAI Deploy App SDK 0.1.0

---


### [REQ]  Support for Object Detection
The SDK shall support developing an application that performs object detection with a pre-trained AI model so that the app developer can incorporate necessary model inputs, transforms, inference and package output from inference in appropriate domain-specific manners.


#### Background
The aim of object detection is to provide a 2D/3D bounding obox around an object of interest. An example is to generate a 3D region of interest for Lung given a  CT dataset.


#### Verification Strategy
Use a pre-trained model designed for object detection. Verify that the SDK provides built-in operators using which an app can be built with that pre-trained model 


#### Target Release
MONAI Deploy App SDK 0.2.0

---


### [REQ]  Supporting models trained with PyTorch
The SDK shall enable app developer to use model trained with PyTorch in an Application so that tasks like model loading, provisioning of input data, a mechanism to perform custom transforms are handled by the SDK

#### Background
PyTorch is open source machine learning framework that accelerates the path from research prototyping to production deployment. It is very popular among healthcare researchers and cmmercial vendors

#### Verification Strategy
Verify that a PyTorch based model can be used to build an application that performs classification, segmentation and object detetcion tasks


#### Target Release
MONAI Deploy App SDK 0.1.0

---


### [REQ]  Supporting models trained with TensorFlow
The SDK shall enable app developer to use model trained with TensorFlow in an Application so that tasks like model loading, provisioning of input data, a mechanism to perform custom transforms are handled by the SDK

#### Background
TensorFlow is an end-to-end open source platform for machine learning. It has a comprehensive, flexible ecosystem of tools, libraries and community resources that lets researchers push the state-of-the-art in ML and developers easily build and deploy ML powered applications.

#### Verification Strategy
Verify that a TensforFlow based model can be used to build an application that performs classification, segmentation and object detetcion tasks


#### Target Release
MONAI Deploy App SDK 0.2.0

---


### [REQ] Supporting MMAR
The SDK shall allow integration of a Clara Train generated Medical Model ARchive (MMAR) for the purpose of inference so that app developers can easily incorporate trained models into a functional application


#### Background
MMAR defines the standard structure for storing artifacts (files) needed and produced by the model development workflow (training, validation, inference, etc.). The MMAR includes all the information about the model including configurations and scripts to provide a work space to perform different model development tasks. In the context of the MONAI App SDK, the relevant usage for the MMAR is for the purpose of inference

#### Verification Strategy
Use an existing MMAR from the Clara Train Repository. Verify that the App SDK provides built-in mechanisms to incorporate the model inherent in the MMAR to perform inference

#### Target Release
MONAI Deploy App SDK 0.1.0

---

### [REQ] Supporting Triton
The SDK shall allow performing inference with a pre-trained AI model via Triton using its supported networking protocol so that app developers can leverage high performance and high utilization of CPU/GPU resources when deployed in a production environment

#### Background
Triton Inference Server provides a cloud and edge inferencing solution optimized for both CPUs and GPUs. Triton supports an HTTP/REST and gRPC protocol that allows remote clients to request inferencing for any model being managed by the server. 

#### Verification Strategy
Use a pre-trained model to develop an application using the App SDK. Verify that the application can be designed in such a way so that the app can leverage Triton at run-time without the app developer explicitly making use of Triton API

#### Target Release
MONAI Deploy App SDK 0.1.0

---




### [REQ]  Integration with DICOM aware systems via MONAI Medical Informatics Gateway
The SDK shall enable applications to integrate with the MONAI Informatics Gateway so that imaging informatics data can be ingested from and exported to clinical informatics system using DICOM as a protocol

#### Background
MONAI Informatics Gateway is a subsystem of the MONAI Deploy platform which facilitates integration with DICOM & FHIR compliant systems, enables ingestion of imaging data, helps triggering of jobs with configurable rules and offers pushing the output of jobs to PACS & EMR systems

#### Verification Strategy
Design an app which ingests DICOM SOP Instances as input and generates DICOM SOP Instances as output. Verify that the input can be provided from the MONAI Informatics Gateway and outputs can be pushed to the MONAI Informatics Gateway.

#### Target Release
MONAI Deploy App SDK 0.1.0

---

### [REQ]  Integration with FHIR aware systems via MONAI Medical Informatics Gateway
The SDK shall enable applications to integrate with the MONAI Informatics Gateway so that healthcare records can be ingested from and exported to clinical informatics system using FHIR as a specification

#### Background
MONAI Informatics Gateway is a subsystem of the MONAI Deploy platform which facilitates integration with DICOM & FHIR compliant systems, enables ingestion of imaging data, helps triggering of jobs with configurable rules and offers pushing the output of jobs to PACS & EMR systems

#### Verification Strategy
Design an app which ingests FHIR Records as input and generates FHIR Records as output. Verify that the input can be provided from the MONAI Informatics Gateway and outputs can be pushed to the MONAI Informatics Gateway.

#### Target Release
MONAI Deploy App SDK 0.1.0

---


### [REQ] Parsing one or more DICOM series
The SDK shall enable filtering a set of DICOM Series with user defined parsing criteria expressed in terms of a collection of keys-value pairs where each key represents a DICOM Attribute so that at run-time appropriate inputs can be provided to the application.

#### Background
Given a collection of DICOM studies, often an app developer needs to figure out which studies and which series belonging to a study are relevant for a specific application. DICOM SOP Instances have a collection of attributes embedded in them. These atributes can use used to parse through a collection of series.


#### Verification Strategy
Verify that the App SDK supports forming selection queries using a collection of rules based on DICOM Attributes. Use these rules to select a seof DICOM series.

#### Target Release
MONAI Deploy App SDK 0.1.0

---


### [REQ] Loading a DICOM 2d/3d dataset into a unified domain object
The SDK shall enable applications to load a 2D/3D imaging dataset belonging to a single DICOM series into a unified "Image" domain object so that downstream operators can process this domain object based on application's needs such as transformation and inference.

#### Background
DICOM as a protocol offers mechanism to represent 2D/3D imaging datasets and corresponding metadata. It is not trivial for application developers to load pixel data from DICOM Part 10 files or messages into a Tensor and associated attributes that qualify the tensor. Having such a mechanism will facilitate easy ingestion of DICOM data in a medical AI application.

#### Verification Strategy
Load  DICOM series into the supported Domian Object using the App SDK. Write out the content of the domain object to disk. Compare that with gold input and verify it matches.

#### Target Release
MONAI Deploy App SDK 0.1.0

---

### [REQ] Supporting DICOM Segmentation Storage SOP Class as output
The SDK shall provide a mechanism to generate a Segmentation Storage SOP Instance where each pixel/voxel can belong to a single category among multiple supported categories. This operator shall be able to output a multi-frame image representing a classification of pixels where each frame represents a 2D plane or a slice of a single segmentation category

#### Background
Healthcare AI apps create segmentation instances during acquisition, post-processing, interpretation and treatment. DICOM Segmentation Storage SOP class provides a way to encode segmentation data. It is intended for composite data objects of any modality or clinical specialty. Segmentations are either binary or fractional.

#### Verification Strategy
Make use of a segmentation model from MONAI core to develop an app. Verify that the output can be exported as a compliant Segmentation Storage SOP Instance

#### Target Release
MONAI Deploy App SDK 0.1.0

---


### [REQ] Supporting DICOM RT Structure Storage SOP Class as Output
The SDK shall provide an operator that supports generating and exporting a RT Structure Set Storage SOP Instance.

#### Background
TBD


#### Verification Strategy
TBD

#### Target Release
MONAI Deploy App SDK 0.1.0

---

### [REQ] GPU Accelerated Primitives
The SDK shall allow support for incorporating common GPU accelerated image processing and computer vision primitives in an Operator
App Verification

#### Background
TBD

#### Verification Strategy
TBD

#### Target Release
MONAI Deploy App SDK 0.1.0

---


### [REQ] App Verification
The SDK shall enable app verification at two levels: operator, application

#### Background
TBD

#### Verification Strategy
TBD

#### Target Release
MONAI Deploy App SDK 0.1.0

---

### [REQ] App Analytics
The SDK shall allow analyzing performance of the application at multiple levels: application, operator, kernel

#### Background
TBD

#### Verification Strategy
TBD

#### Target Release
MONAI Deploy App SDK 0.2.0

---


### [REQ] Data Visualization
The SDK shall enable 2D/3D/4D medical image visualization of input, intermediate artifacts & output of an application during development

#### Background
TBD

#### Verification Strategy
TBD

#### Target Release
MONAI Deploy App SDK 0.2.0

---

### [REQ] Data Specification for App
The SDK shall enable developers to specify conditions so that the right input datasets can be routed to an app during execution

#### Background
TBD

#### Verification Strategy
TBD

#### Target Release
MONAI Deploy App SDK 0.1.0

---


### [REQ] App Resource Requirements

#### Background
TBD

The SDK shall enable developers to specify desired resource requirements (GPU Memory, System Memory), for the application during app development

#### Verification Strategy
TBD

#### Target Release
MONAI Deploy App SDK 0.1.0

---

### [REQ] Existing Containers
The SDK shall support use of an existing container image as the base for designing an Operator

#### Background
TBD

#### Verification Strategy
TBD

#### Target Release
MONAI Deploy App SDK 0.1.0

---

### [REQ] Packaging an Application
The SDK shall allow packaging of the application in a standardized format so that it can be executed by a compliant runtime environment

#### Background
TBD

#### Verification Strategy
TBD

#### Target Release
MONAI Deploy App SDK 0.1.0



### [REQ]  Execution of Application
The SDK shall allow execution of an application in the developer's workstation.

#### Background
TBD

#### Verification Strategy
TBD

#### Target Release
MONAI Deploy App SDK 0.1.0


### [REQ] Development Console
The SDK shall provide a Development Console to track activities during designing of an application

#### Background
TBD

#### Verification Strategy
TBD

#### Target Release
MONAI Deploy App SDK 0.2.0