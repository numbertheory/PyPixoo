---
title: Getting Started
position_number: 2
parameters:
  - name:
    content:
content_markdown: |-
  Make sure you've successfully connected your Pixoo64 to your local wifi network and
  can normally interact with the device via your phone. Don't try to use this wrapper
  until you've done at least that.

  It's also a good idea to set your router so that the Pixoo64 is assigned a static
  IP address for your network (assigned via MAC address). That way, when your router has to restart,
  you won't lose your IP address assignment.

  Finally, run this command from your command line to make sure you can interact with the device
  programatticaly.
left_code_blocks:
  - code_block: "curl -X POST http://<IP Address>:80/post -d '{\"Command\": \"Channel/GetIndex\"}'"
    title:
    language: Bash
right_code_blocks:
  - code_block:
    title:
    language:
---