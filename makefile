# makefile, p_video/


target: clean
.PHONY: target

clean: clean_py
.PHONY: clean


clean_py: .clean_py.flag
.PHONY: clean_py

PYC_FILE=$(shell find . | grep "\.pyc$$")
PYC_DIR=$(shell find . | grep "__pycache__")

.clean_py.flag: $(PYC_FILE) $(PYC_DIR)
	- find . | grep "\.pyc$$" | xargs rm
	- find . | grep "__pycache__" | xargs rmdir
	touch .clean_py.flag


# end makefile


