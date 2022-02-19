# Flags
  Flag Variant:
      None.
      c.
      d.
      D.
      cd.
      dD.       [single]
      Flags other than r and d.     [error]

# Files
  Input file:
      Single file.
      Non-existent file.        [error]
      No file.     [property noInFile]
      Hyphen.
  Output file:
      Single file.      [if !noInFile]
      Non-existent file.        [if !noInFile]
      No file.
      Hyphen.       [if !noInFile]

# Edge Case
  Edge Case:
      More than 2 operands.     [error]