import kfp
from kfp import dsl
from kubernetes.client.models import V1EnvVar

ver = '1.0'

@dsl.pipeline(
    name = 'Tibero-ML-pipeline',
    description = 'A Machine Learning pipeline with Tibero JDBC agent'
)

def ml_pipeline():
    pvc1 = dsl.VolumeOp(
        name = "PVC-data",
        resource_name = "pvc-ojt-ml",
        storage_class = "ojt-tibero-ml",
        modes = dsl.VOLUME_MODE_RWM,
        size = "1Gi"
    )

    pvc2 = dsl.VolumeOp(
        name = "PVC-was",
        resource_name = "pvc-ojt-result",
        storage_class = "ojt-tibero-result",
        modes = dsl.VOLUME_MODE_RWM,
        size = "1Gi"
    )

    pod1 = dsl.ContainerOp(
        name = 'Tibero-JDBC agent',
        image = 'hanjoo8821/jdbc-tibero:colsout-' + ver,
        container_kwargs={'env':[V1EnvVar('id', 'hanjoo'), V1EnvVar('pw', '1010'), V1EnvVar('sql', 'SELECT * FROM AB1_2 LEFT JOIN ACCOUNTING ON AB1_2.EMP_NUM = ACCOUNTING.EMP_NUM'), V1EnvVar('col1', 'EMP_NUM'), V1EnvVar('col2', 'BIRTH'), V1EnvVar('col3', 'SALARY')]},
        pvolumes = {"/Output": pvc1.volume}
    )

    pod2a = dsl.ContainerOp(
        name = 'Print-EMP_NUM',
        image = 'alpine:3.6',
        command = ['cat', '/Output/EMP_NUM.txt'],
        pvolumes = {"/Output": pod1.pvolume}
    )

    pod2b = dsl.ContainerOp(
        name = 'Trans-BIRTH',
        image = 'hanjoo8821/jdbc-tibero:trans-birth-' + ver,
        container_kwargs={'env':[V1EnvVar('col2', 'BIRTH')]},
        pvolumes = {"/Output": pod1.pvolume}
    )

    pod2c = dsl.ContainerOp(
        name = 'Trans-SALARY',
        image = 'hanjoo8821/jdbc-tibero:trans-salary-' + ver,
        container_kwargs={'env':[V1EnvVar('col3', 'SALARY')]},
        pvolumes = {"/Output": pod1.pvolume}
    )

    pod3 = dsl.ContainerOp(
        name = 'ML-Linear Regression',
        image = 'hanjoo8821/jdbc-tibero:ml-' + ver,
        container_kwargs={'env':[V1EnvVar('col2', 'BIRTH'), V1EnvVar('col3', 'SALARY')]},
        pvolumes = {"/Output": pod2b.pvolume}
    ).after(pod2b, pod2c)

    pod4 = dsl.ContainerOp(
        name = 'Visualization',
        image = 'hanjoo8821/jdbc-tibero:graph-' + ver,
        container_kwargs={'env':[V1EnvVar('col2', 'BIRTH'), V1EnvVar('col3', 'SALARY')]},
        pvolumes = {"/Output": pod3.pvolume, "/WAS": pvc2.volume}
    )

    # pvc1.delete().after(pod4) # 삭제 시 보호설정 해지 명령 추가: kubectl -n kubeflow patch pvc pvc-ojt-ml -p '{"metadata":{"finalizers":null}}'
    # pvc2.delete().after(pod4) # 삭제 시 보호설정 해지 명령 추가: kubectl -n kubeflow patch pvc pvc-ojt-result -p '{"metadata":{"finalizers":null}}'

if __name__ == '__main__':
    kfp.compiler.Compiler().compile(ml_pipeline, __file__ + '.tar.gz')