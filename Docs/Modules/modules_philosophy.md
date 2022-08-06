# Modules Philosophy

Modules are the building bricks of the AI. This structure allows easy construction and modification of modules throughout development. All modules will follow the basic structure guidelines to make installation as simple as possible.

## What is the I/O of a module?
- Input
  - A timer event
  - User command initiation
  - Hardware change
  - Digital signal
- Output
  - TTS response
  - Automation event
  - Hardware movement
  - AI change
  - Logging

## Requirements for module
- Communicate with Scheduler
- Be independent
- Cross communicable


## Sample Var standards:
- Instanced
  - `['whatToInstance", ["inputs"]]`

## Module Contents
Each module will have access to these items
- The main config file
- Its own config file
- A resource folder
- Scheduler tabs
- Other modules