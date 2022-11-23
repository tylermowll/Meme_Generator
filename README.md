From the terminal run either meme.py or app.py.

meme.py take optional arguments "path", "body", and author.

app.py will provide prompts to either generate a random meme or find an online image and add a custom body and author.

IngestorInterface.py provides the abstract method for parsing files and determining if the files are compatible.

The various file importer child classes, each defined in its own file, inherit from IngestorInterface.py to import specific file types.

Ingestor.py ties encapsulates all the child classes to tie the import mechanisms together.

MemeEngine creates the meme by taking the image and superimposing body and an author attribution.