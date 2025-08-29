from .dtos import LookSemanaRequestDTO, LookSemanaResponseDTO

class LookSemanaService:
    def gerar_look_semana(self, request_dto: LookSemanaRequestDTO) -> LookSemanaResponseDTO:
        # 1. Validar dados
        if not request_dto.usuario_id:
            raise ValueError("Usuário inválido")

        # 2. Buscar peças disponíveis (simulação)
        pecas_disponiveis = ["Camisa Branca", "Calça Jeans", "Tênis", "Jaqueta", "Camisa Preta"]

        # 3. Aplicar preferências do usuário
        if request_dto.preferencia_estilo == "casual":
            pecas_disponiveis = [p for p in pecas_disponiveis if "Camisa" in p or "Tênis" in p]

        # 4. Considerar clima (simulação)
        observacao = None
        if request_dto.considerar_clima:
            observacao = "Previsão de chuva, incluir jaqueta"

        # 5. Gerar looks para cada dia da semana
        dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]
        looks = {dia: [pecas_disponiveis[i % len(pecas_disponiveis)]] for i, dia in enumerate(dias)}

        # 6. Retornar DTO de resposta
        return LookSemanaResponseDTO(
            usuario_id=request_dto.usuario_id,
            semana_referencia=request_dto.semana_referencia or "2025-09-01 a 2025-09-07",
            looks=looks,
            observacao=observacao
        )
