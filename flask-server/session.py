import uuid

from typing import Any, Dict
from datetime import datetime

def session(category, questions: Dict[str, Any]) -> Dict[str, Any]:
    return {
        'id': str(uuid.uuid4()),
        'created': datetime.now(),
        'updated': datetime.now(),
        'category': category,
        'questions': questions
    }
