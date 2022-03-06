# Flags
  Flag Variant:
      None.
      r.    [property hasRFlag]
      d.
      rd.   [single]
      Flags other than r and d.     [error]

# Files
  File variant:
      Single file.
      Multiple files.
      No such file.     [single]
      No file.
      Single dot.   [if hasRFlag][error]
      Double dot.   [if hasRFlag][error]
      Single slash.   [if hasRFlag][error]

# Folders
  Folder variant:
      Empty folder.
      Non-empty folder.
      Multiple folders.
      No such folder.       [single]
      No folder.
