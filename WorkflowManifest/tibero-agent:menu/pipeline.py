import kfp
from kfp import dsl

def query_op():
    return dsl.ContainerOp(
        name = "JDBC Agent",
        image = "hanjoo8821/jdbc-tibero:menu"
    )

@dsl.pipeline(
    name = "tibero-agent:menu",
    description = "Hanjoo's tibero agent : menu version"
)

def tibero_pipeline_menu():
    tibero = query_op()
    
if __name__ == "__main__":
    kfp.compiler.Compiler().compile(tibero_pipeline_menu, __file__ + ".tar.gz")