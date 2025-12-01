% rebase('layout', title='Lançar Faltas')

<h2>Lançar Faltas</h2>
<p>Professor: {{prof.name}}</p>

<form method="post" action="/lancar_faltas">
    <label for="disciplina_id">Disciplina:</label>
    <select id="disciplina_id" name="disciplina_id" required>
        <option value="">Selecione uma turma</option>
        % for turma in minhas_turmas:
        <option value="{{turma.id}}">{{turma.codigo}} - {{turma.nome}} (Turma {{turma.turma}})</option>
        % end
    </select><br>
    
    <label for="aluno">Aluno:</label>
    <input type="text" id="aluno" name="aluno" required><br>
    
    <label for="faltas">Quantidade de Faltas:</label>
    <input type="number" id="faltas" name="faltas" min="0" required><br>
    
    <button type="submit">Lançar Faltas</button>
</form>
