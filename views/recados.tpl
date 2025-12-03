% rebase('layout', title='Recados', nav_dict=nav_dict)

% if modo == 'professor':
<div class="form-section" style="max-width: 700px;">
    <h1>💬 Enviar Recado</h1>
    % if 'mensagem_sucesso' in locals() and mensagem_sucesso:
        <div class="card" style="background-color: var(--success-light); border-color: var(--success-color);">
            <p style="color: var(--success-color);">✅ {{mensagem_sucesso}}</p>
        </div>
    % end
    <form method="post" action="/enviar_recado" class="form-container">
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
            <label for="titulo">Título:</label>
            <input type="text" id="titulo" name="titulo" required>
        </div>
        <div class="form-group">
            <label for="mensagem">Mensagem:</label>
            <textarea id="mensagem" name="mensagem" rows="5" required></textarea>
        </div>
        <div class="form-group">
            <label for="aluno_id">Direcionar para aluno específico (opcional):</label>
            <input type="number" id="aluno_id" name="aluno_id" placeholder="ID do aluno">
        </div>
        <div class="form-actions">
            <button type="submit" class="btn-submit">📤 Enviar</button>
            <button onclick="window.location.href='/dashboard/professor'" class="btn-cancel" style="text-decoration: none;">Voltar</button>
        </div>
    </form>
    </div>
% elif modo == 'aluno':
<div class="welcome-section">
    <h1>💬 Meus Recados</h1>
    <p>Mensagens de professores das suas disciplinas</p>
</div>
% if not recados:
    <div class="card"><p style="text-align:center; color: var(--text-light);">Nenhum recado no momento.</p></div>
% else:
    % for r in recados:
        <div class="card">
            <div class="card-header">
                <h3 class="card-title">{{r.titulo}}</h3>
                <span class="badge badge-info">{{r.disciplina_codigo or 'Geral'}}</span>
            </div>
            <div class="card-body">
                <p>{{r.mensagem}}</p>
            </div>
        </div>
    % end
% end
<div style="margin-top: 20px; text-align: center;">
    <button onclick="window.location.href='/dashboard/aluno'" class="btn-cancel" style="text-decoration: none;">🏠 Voltar</button>
</div>
% end