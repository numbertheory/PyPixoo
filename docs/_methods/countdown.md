---
title: countdown
position_number: 1.3
type: post
description: Set the Countdown timer
parameters:
  - name: minute
    type: integer
  - name: second
    type: integer
content_markdown: |-
  This sets a countdown timer on the device. When it reaches zero, the device produces a short alarm and
  resets to a 1 minute timer.
left_code_blocks:
  - code_block: |-
      >>> from pypixoo import device
      >>> d = device.Pixoo64(ip="192.168.X.X")
      >>> d.countdown(1, 10) # sets a countdown for 1 minute and 10 seconds
    title: Python
    language: Python
right_code_blocks:
  - code_block: |-
      [200, {'error_code': 0}]
    title: Response
    language: python
---

