from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class LookSemanaRequestDTO:
    usuario_id: int
    pecas_selecionadas: Optional[List[int]] = None
    preferencia_estilo: Optional[str] = None
    considerar_clima: bool = False
    semana_referencia: Optional[str] = None

@dataclass
class LookSemanaResponseDTO:
    usuario_id: int
    semana_referencia: str
    looks: Dict[str, List[str]]
    observacao: Optional[str] = None
