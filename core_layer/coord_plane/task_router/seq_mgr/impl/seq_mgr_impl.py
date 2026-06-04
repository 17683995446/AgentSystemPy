from ..interfaces.i_seq_mgr import ISeqMgr


class SeqMgrImpl(ISeqMgr):
    def create_seq(self, items: list[dict]) -> dict:
        seq = {"items": items, "status": "created"}
        return seq

    def reorder_seq(self, seq: dict, order: list[int]) -> dict:
        items = [seq["items"][i] for i in order if 0 <= i < len(seq["items"])]
        return {"items": items, "status": "reordered"}

    def validate_seq(self, seq: dict) -> bool:
        valid = isinstance(seq.get("items"), list)
        return valid

    def execute_seq(self, seq: dict) -> dict:
        result = {"seq": seq, "status": "executed"}
        return result
