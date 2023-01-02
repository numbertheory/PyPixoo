---
title: currentChannel
position_number: 1.1
type: post
description: Get the current Channel
content_markdown: |-
  This will return a Python list. 
  The first item is the status code for the request.
  The second item is the response as a Python dictionary.
left_code_blocks:
  - code_block: |-
      >>> from pypixoo import device
      >>> d = device.Pixoo64(ip="192.168.X.X")
      >>> d.getChannel()
    title: Python
    language: Python
right_code_blocks:
  - code_block: |-
      [200, {'error_code': 0, 'SelectIndex': 2}]
    title: Response
    language: python
---


