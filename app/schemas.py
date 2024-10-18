from pydantic import BaseModel
class TrainTaskBase(BaseModel):
    id: str
    name: str
    type: str
    status: int
    path: str
    sample_set_id: str
    pretrain_model_id: str
    uid: int
    start_time: str
    end_time: str
    delete_flag: bool



class createModelReq(BaseModel):
    type: str = ""
    name: str = ""
    description: str = ""
    useGPU: bool = 0
    memory: int = 1024
    eporch: int = 10
    batchSize: int = 4
    iou: float = 0.3
    uid: int = 0

