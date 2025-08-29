from src.looksy.dtos import LookSemanaRequestDTO  
from src.looksy.service import LookSemanaService

if __name__ == "__main__":
    service = LookSemanaService()
    
    # Criar RequestDTO de exemplo
    request = LookSemanaRequestDTO(
        usuario_id=1,
        preferencia_estilo="casual",
        considerar_clima=True
    )

    # Gerar look da semana
    response = service.gerar_look_semana(request)
    
    # Imprimir resultado
    print(response)
