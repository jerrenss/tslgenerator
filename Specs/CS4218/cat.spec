# Flags
  Flag Variant:
      n.
      None.
      Flags other than r and d.     [error]

# Files
  File variant:
      Single file.
      Multiple files.
      Non existent file.     [error]
      Multiple files with some non-existent.   [error]
      No file.
      Single folder.   [error]
      Multiple files with a folder.    [error]

# Stdin
  Hyphen variant:
      1.      [property hasStdin]
      0.
      More than 1.    [single]

  Hyphen location:
      Before file.       [if hasStdin][single]
      Before files.       [if hasStdin][single]
      After file.        [if hasStdin][single]
      After files.        [if hasStdin][single]
      Between files.        [if hasStdin][single]
