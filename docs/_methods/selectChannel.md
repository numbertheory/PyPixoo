---
title: selectChannel
position_number: 1.1
type: post
description: Select the channel
content_markdown: |-
  This will return a list

  Adds a book to your collection.
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

