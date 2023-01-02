---
title: brightness
position_number: 1.4
type: post
description: Select the channel
parameters:
  - name: brightness
    content: "Set as an integer, 1-100."
content_markdown: |-
  This changes the brightness of the screen. 100 is the default brightness.
left_code_blocks:
  - code_block: |-
      >>> from pypixoo import device
      >>> d = device.Pixoo64(ip="192.168.X.X")
      >>> d.brightness(10)
      >>> d.brightness(99)
    title: Python
    language: Python
right_code_blocks:
  - code_block: |-
      [200, {'error_code': 0}]
    title: Response
    language: python
---

