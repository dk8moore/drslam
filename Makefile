# Makefile with useful commands
.PHONY: help tree

tree:
	# Print the directory tree to a file
	tree -a -I '.venv|venv|__pycache__|node_modules|.git|.gitignore|Makefile|.vscode|.DS_Store|staticfiles|tree.txt' --dirsfirst > tree.txt