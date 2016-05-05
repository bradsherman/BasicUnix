Reading 06
==========

1. I would use the command $ echo "All your base are belong to us" |tr [:lower:] [:upper:]
2. I would use the command $ grep "^root" /etc/passwd | awk -F":" '{print $7}'
3. I would use the command $ sed -i -e 's/monkeys/gorillaz/g' filename
	alternatively ->>  $ echo "monkeys love bananas" | sed 's/monkeys/gorillaz/g'
4. I would use the command $ cat /etc/passwd | sed -r 's@/bin/(bash|csh|tcsh)@/usr/bin/python@' | grep python
5. I would use the command $ echo "     monkeys love bananas" | sed 's/^\s*//'
6. I would use the command $ cat /etc/passwd | sed -rn '/4[0-9]*7/p'
7. I would use the command $ tail -f file1 file2 file3...
8. I would use the command $ comm -12 file1 file2
