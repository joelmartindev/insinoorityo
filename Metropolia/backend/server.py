from transformers import pipeline

pipe = pipeline("translation_en_to_fi", model="Helsinki-NLP/opus-mt-en-fi")
print(pipe("This restaurant is awesome"))

homma = pipe("Translation is fun")
print(homma)

def data():
    while True:
        # This could come from a dataset, a database, a queue or HTTP request
        # in a server
        # Caveat: because this is iterative, you cannot use `num_workers > 1` variable
        # to use multiple threads to preprocess data. You can still have 1 thread that
        # does the preprocessing while the main runs the big inference
        yield "This is a test"
        yield "This a test as well"
        return


for out in pipe(data()):
    print(out)