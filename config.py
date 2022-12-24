#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @DarkzzAngel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 22195812))
    API_HASH = os.environ.get("API_HASH", b404c7b3066992e62ae39640576647eb)
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5495307325:AAHU2cZAo9EhkJ1Un0v06lA-ZBrIhY3_Izs") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "document")
    OWNER_ID = os.environ.get("OWNER_ID", 794968418)
    SESSION = os.environ.get("SESSION", AQAq5FZsHTK0nnJvkLUlYdkDJharBVUgWRXsfXLu7IQVAWySkGl23x-TQ4hwcnpo5VeSLBs3rdYgqf4jmMoqaR5uU_fmvDJI_6fzvnlCajQKIaJp9MySXPbMChhQrY7KmUT_kM7EMtFQ7X6CKRGlSOMrjuKo8fzF-XQohCkDBhmxT3SoOcb1xjhebVJsJAC_1KR-YYfFLmyEGXR58_JIf9jf1LB30QBFhRCgTXjJb6c9x3U1HWqttbmGvulEmHynOgX4H6508EpDmm-c-qnwfeeWTRk1BmiCJfJEuu4smFRD_tMI54lBR6FFwUpvRWLf4OXfNcrDOUgErP3IISdZIgchAAAAAVxsbRQA)
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
