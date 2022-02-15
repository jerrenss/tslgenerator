# Command
  Command Variant:
      Single.
      Multiple.      [property hasMultipleCommands]

  Command Response:
      All successful.
      At least one throwing exception.
      All throwing exception.     [if hasMultipleCommands]

# Semicolon
  Semicolon variant:
      Extra semicolon at start.     [single]
      Extra semicolon at end.     [single]
      Duplicated semicolons at start.     [error]
      Duplicated semicolons at end.     [error]
      Duplicated semicolons in between.     [error][if hasMultipleCommands]
      Single semicolon with no commands.     [single]
      Duplicated semicolons with no commands.     [error]
      Multiple semicolons with space in between.     [single]

