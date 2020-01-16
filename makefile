grade:
	for f in Submissions/*;	\
	do		\
		echo "$$f";	\
		cp $$f Test.py;	\
		$(PYTHON) Grade.py
	done;		\

update:
	git status
	git add *