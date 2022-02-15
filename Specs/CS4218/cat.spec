# Flags
  Flag Variant:
      n.
      None.
      Flags other than r and d.     [error]

# Files
  File variant:
      Single file.
      Multiple files.
      No such file.     [single]
      No file.

# Stdin
  Stdin variant:
      Present.      [property hasStdin]
      Absent.
  Stdin location:
      Before file.       [if hasStdin][single]
      Before files.       [if hasStdin][single]
      After file.        [if hasStdin][single]
      After files.        [if hasStdin][single]
      Between files.        [if hasStdin][single]
