Temporarily switch to a different commit
This will detach your HEAD, that is, leave you with no branch checked out:
```
git checkout 0d1d7fc32
```

Or if you want to make commits while you're there, go ahead and make a new branch while you're at it:
```
git checkout -b old-state 0d1d7fc32
```

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

Vim regex: matching a literal word, excluding sub-strings

```
gd :%s//string/g
```

Format multiple files from command line:

```
for i in ./*.{php,js,cpp,sh}; do
    vim -c "normal gg=G" -c "x" $i
done
```
Add text to the start and/or end of line

```
:%s/^\(.*\)/"\1"/
```

Temporarily switch to a different commit
This will detach your HEAD, that is, leave you with no branch checked out:
`git checkout 0d1d7fc32`

Replace a string in multiple files in linux command line
Occurrences of foo will be replaces with bar
```
cd /path/to/your/file
sed -i 's/foo/bar/g' *
```

clone private/ any repo github

```
git clone https://[TOKEN]@github.com/[REPO-OWNER]/[REPO-NAME]
```

Visually select all the lines you want to increment, and do the following:

```
:s/\d\+/\=submatch(0) + 132

```

Schedule a bash command later in time:
```
at 1200 << EOF
bash command
EOF
```
