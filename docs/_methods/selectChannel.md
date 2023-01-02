---
title: selectChannel
position_number: 1.2
type: post
description: Select the channel
parameters:
  - name: channel
    type: string
    content: "Options are: \"faces\", \"cloud\", \"visualizer\",\"custom\", \"blank\""
content_markdown: |-
  This changes face of the clock to the various channels. 
   - Cloud: The channel that is controlled by the phone app. Random designs.
   - Faces: The channel that shows the time using whatever clock face is selected.
   - Visualizer: An audio visualizer of the room, picked up by the Pixoo64.
   - Blank: Screen turns off.
left_code_blocks:
  - code_block: |-
      >>> from pypixoo import device
      >>> d = device.Pixoo64(ip="192.168.X.X")
      >>> d.selectChannel("cloud") # changes channel to cloud channel
      >>> d.selectChannel("faces") # changes to clock faces
      >>> d.selectChannel("visualizer") # changes to audio visualizer
      >>> d.selectChannel("blank") # changes to a blank screen
    title: Python
    language: Python
right_code_blocks:
  - code_block: |-
      [200, {'error_code': 0}]
    title: Response
    language: python
---

