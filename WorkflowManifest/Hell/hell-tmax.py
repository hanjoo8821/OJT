import kfp
from kfp import dsl

def hell_op(n):
    return dsl.ContainerOp(
        name = n,
        image = "hanjoo8821/hell:ex"
    )

@dsl.pipeline(
    name = "print",
    description = "print test"
)

def hello_goodbye(): 
    pod1 = hell_op("Hello")
    pod2a = hell_op("Postech").after(pod1)
    pod2b = hell_op("Tmax").after(pod1)
    pod3 = hell_op("Goodbye").after(pod2a, pod2b)
    
if __name__ == "__main__":
    kfp.compiler.Compiler().compile(hello_goodbye, __file__ + ".tar.gz")