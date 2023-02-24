The ex *command g* is very useful for acting on lines that match a pattern. You can use it with the d command, to delete all lines that contain a particular pattern, or all lines that do not contain a pattern.

For example, to delete all lines containing "profile" (remove the /d to show the lines that the command will delete):

```
:g/profile/d
```

More complex patterns can be used, such as deleting all lines that are empty or that contain only whitespace:

```
:g/^\s*$/d
```

To delete all lines that do not contain a pattern, use g!, like this command to delete all lines that are not comment lines in a Vim script:

```
:g!/^\s*"/d
```

Note that g! is equivalent to v, so you could also do the above with:

```
:v/^\s*"/d
```

The next example shows use of \| ("or") to delete all lines except those that contain "error" or "warn" or "fail" (:help pattern):

```
:v/error\|warn\|fail/d
```
