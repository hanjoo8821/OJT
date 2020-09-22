import kfp
from kfp import dsl
from kubernetes.client.models import V1EnvVar

def query_op(n):
    return dsl.ContainerOp(
        name = n,
        image = "hanjoo8821/jdbc-tibero:basic",
        container_kwargs = {'env': [V1EnvVar('id', 'hanjoo'), V1EnvVar('pw', '1010')]}
    )

@dsl.pipeline(
    name = "tibero-agent:basic",
    description = "Hanjoo's tibero agent : basic version"
)

def tibero_pipeline_basic():
    sql1 = query_op("SQL1")
    sql2a = query_op("SQL2a").after(sql1)
    sql2b = query_op("SQL2b").after(sql1)
    sql3 = query_op("SQL3").after(sql2a, sql2b)
    
if __name__ == "__main__":
    kfp.compiler.Compiler().compile(tibero_pipeline_basic, __file__ + ".tar.gz")