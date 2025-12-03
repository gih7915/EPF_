% rebase('layout', title='Criar Atividade', nav_dict=nav_dict)

<div class="form-section" style="max-width: 700px;">
    <h1>📚 Criar Nova Atividade</h1>
    
    <form method="post" action="/criar_atividade" class="form-container">
        <div class="form-group">
            <label for="disciplina_codigo">Disciplina:</label>
            <select id="disciplina_codigo" name="disciplina_codigo" required>
                <option value="">Selecione uma disciplina</option>
                % for turma in minhas_turmas:
                    <option value="{{turma.codigo}}">{{turma.codigo}} - {{turma.nome}} (Turma {{turma.turma}})</option>
                % end
            </select>
        </div>

        <div class="form-group">
            <label for="titulo">Título da Atividade:</label>
            <input type="text" id="titulo" name="titulo" placeholder="Ex: Lista de Exercícios 1" required>
        </div>

        <div class="form-group">
            <label for="descricao">Descrição:</label>
            <textarea id="descricao" name="descricao" rows="5" placeholder="Descreva os objetivos e requisitos da atividade..." required></textarea>
        </div>

        <div class="form-group">
            <label for="prazo">Prazo de Entrega:</label>
            <input type="date" id="prazo" name="prazo" required>
        </div>

        <div class="form-actions">
            <button type="submit" class="btn-submit">✅ Criar Atividade</button>
            <button type="button" onclick="window.location.href='/dashboard/professor'" class="btn-cancel">Cancelar</button>
        </div>
    </form>
</div>
