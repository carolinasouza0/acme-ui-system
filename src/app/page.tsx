"use client";

import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Loader2 } from "lucide-react"; // Um ícone de loading nativo do lucide!

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!prompt.trim()) return;

    setIsLoading(true);
    setResponse(""); // Limpa a tela para a nova resposta

    try {
      // Faz a requisição para a nossa API Python que está no Docker
      const res = await fetch("http://localhost:8000/api/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: prompt }),
      });

      const data = await res.json();
      
      if (data.response) {
        setResponse(data.response);
      } else {
        setResponse("⚠️ Erro retornado pela API: " + JSON.stringify(data.error));
      }
    } catch (error) {
      setResponse("🚨 Erro crítico: Não foi possível conectar ao Agente. Verifique se a API está rodando na porta 8000.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-slate-50 flex flex-col items-center justify-center p-4">
      <Card className="w-full max-w-3xl shadow-lg">
        <CardHeader className="bg-slate-900 text-white rounded-t-xl">
          <CardTitle className="text-2xl">🤖 UI-Gen Architect</CardTitle>
          <CardDescription className="text-slate-300">
            Peça qualquer componente. O agente usará estritamente o nosso Design System.
          </CardDescription>
        </CardHeader>
        
        <CardContent className="p-6 space-y-6">
          <form onSubmit={handleSubmit} className="flex gap-3">
            <Input
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="Ex: Crie um formulário de login com email e senha..."
              disabled={isLoading}
              className="text-base"
            />
            <Button type="submit" disabled={isLoading} className="w-32">
              {isLoading ? (
                <>
                  <Loader2 className="mr-2 h-4 w-4 animate-spin" />
                  Gerando...
                </>
              ) : (
                "Gerar Código"
              )}
            </Button>
          </form>

          {response && (
            <div className="mt-6">
              <h3 className="text-sm font-bold text-slate-500 mb-2 uppercase tracking-wider">Resposta do Agente:</h3>
              <div className="bg-slate-950 p-4 rounded-lg overflow-x-auto">
                {/* O código gerado pela IA usa blocos Markdown, a tag <pre> respeita a formatação */}
                <pre className="text-sm text-green-400 font-mono whitespace-pre-wrap">
                  {response}
                </pre>
              </div>
            </div>
          )}
        </CardContent>
      </Card>
    </main>
  );
}