% include('layout.tpl')
<h1>Entregar Tarefa</h1>

<div style="background: #ecf0f1; padding: 15px; border-radius: 4px; margin-bottom: 20px;">
    <p><strong>Tarefa:</strong> {{tarefa.titulo}}</p>
    <p><strong>Disciplina:</strong> {{tarefa.disciplina or 'Geral'}}</p>
    <p><strong>Descrição:</strong> {{tarefa.descricao or ''}}</p>
    % if tarefa.prazo:
        <p><strong>📅 Prazo:</strong> {{tarefa.prazo}}</p>
    % end
    % if tarefa.max_points:
        <p><strong>Valor:</strong> {{tarefa.max_points}} pontos</p>
    % end
</div>

<form method="post" action="/tarefas/submit/{{tarefa.id}}">
    <input type="hidden" name="aluno_id" value="{{aluno_id}}">
    
    <label for="conteudo"><strong>Conteúdo da Entrega</strong></label>
    <textarea id="conteudo" name="conteudo" placeholder="Digite ou cole o conteúdo da sua entrega aqui..." required></textarea>
    
    <label for="entregue_em"><strong>Data de Entrega (YYYY-MM-DD)</strong></label>
    <input id="entregue_em" type="date" name="entregue_em" required>
    
    <div class="item-actions">
        <button type="submit" class="btn btn-success">Enviar Entrega</button>
        <a href="/tarefas?aluno_id={{aluno_id}}" class="btn">Cancelar</a>
    </div>
</form>
