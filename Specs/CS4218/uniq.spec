# Flags
  Flag Variant:
      None.
      c.
      d.
      D.
      cd.
      dD.       [single]
      Flags other than c, d and D.     [error]

# Files
  Input file:
      Single file.
      Non-existent file.        [error]
      Folder.       [error]
      No file.     [property noInFile]
      Hyphen.
  Output file:
      Single file.      [if !noInFile]
      Non-existent file.        [if !noInFile][single]
      Folder.       [if !noInFile][error]
      No file.
      Hyphen.       [if !noInFile][single]

# Edge Case
  Edge Case:
      More than 2 operands.     [error]