"""The decode-floor v1 helper baked into image ef9f5013 (identity v1-image-d9758a6).

Inserted at the patcher's NEEDLE with the v1 hook pairs, it rebuilds that image's
scheduler.py byte-for-byte from the pristine source.
"""
HELPER = '\ndef _glm53_mixed_prefill_policy(running, current):\n    """Mixed-step prefill policy when a peer in `running` is decoding.\n\n    None = no extra policy. 0 = skip this prefill this step. N>0 = cap.\n    """\n    raw = os.environ.get("GLM53_MIXED_PREFILL_CHUNK", "0").strip().lower()\n    if raw in ("0", "off", "no"):\n        return None\n    if raw in ("skip", "-1"):\n        cap = 0\n    else:\n        try:\n            cap = int(raw)\n        except ValueError:\n            cap = 0\n        if cap <= 0:\n            return None\n    cur_id = getattr(current, "request_id", None)\n    for r in running:\n        if r is current or getattr(r, "request_id", None) == cur_id:\n            continue\n        if r.num_computed_tokens >= r.num_prompt_tokens:\n            return cap\n    return None\n\n\n'
