<?php

$request_uri = $_SERVER['REQUEST_URI'];

if ($request_uri === '/payment') {
    try {
        // Criar contexto para a requisição HTTP
        $context = stream_context_create([
            'http' => [
                'timeout' => 10,
                'method' => 'GET'
            ]
        ]);
        
        $orderJson = file_get_contents('http://orders:3002/order', false, $context);
        
        if ($orderJson === false) {
            throw new Exception('Falha ao obter dados do pedido');
        }
        
        $orderData = json_decode($orderJson, true);
        
        if (json_last_error() !== JSON_ERROR_NONE) {
            throw new Exception('Erro ao decodificar JSON: ' . json_last_error_msg());
        }

        $response = [
            'status' => 'paid',
            'order' => $orderData
        ];

        header('Content-Type: application/json');
        echo json_encode($response, JSON_PRETTY_PRINT);
        
    } catch (Exception $e) {
        http_response_code(500);
        header('Content-Type: application/json');
        echo json_encode([
            'error' => 'Erro interno do servidor',
            'message' => $e->getMessage()
        ]);
    }
} else {
    http_response_code(404);
    header('Content-Type: application/json');
    echo json_encode(['error' => 'Not found']);
}

?>