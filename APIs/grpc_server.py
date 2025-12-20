import grpc
from concurrent import futures
import user_service_pb2
import user_service_pb2_grpc

class UserserviceServicer(user_service_pb2_grpc.UserserviceServicer):
    def GetUser(self, request, context):
        print(f"Получен запрос от: {request.username}")

        return user_service_pb2.GetUserResponse(message=f"Привет, {request.username}!")

def serve(): 
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        user_service_pb2_grpc.add_UserserviceServicer_to_server(UserserviceServicer(), server)

        server.add_insecure_port('[::]:50051')
        server.start()
        print("Сервер запущен на порту 50051")
        server.wait_for_termination()

if __name__ == "__main__":
    serve()