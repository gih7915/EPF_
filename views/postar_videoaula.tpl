% rebase('layout', title='Postar Videoaula', nav_dict=nav_dict)

<div class="form-section" style="max-width: 700px;">
    <h1>🎥 Postar Videoaula</h1>
    
    <form method="post" action="/postar_videoaula" class="form-container">
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
            <label for="titulo">Título da Videoaula:</label>
            <input type="text" id="titulo" name="titulo" placeholder="Ex: Aula 1 - Introdução" required>
        </div>

        <div class="form-group">
            <label for="link">Link do Vídeo (YouTube, Vimeo, etc):</label>
            <input type="url" id="link" name="link" placeholder="https://www.youtube.com/watch?v=..." required>
        </div>

        <div class="form-group">
            <label for="descricao">Descrição:</label>
            <textarea id="descricao" name="descricao" rows="5" placeholder="Descreva o conteúdo da videoaula..."></textarea>
        </div>

        <div class="form-actions">
            <button type="submit" class="btn-submit">📤 Publicar Videoaula</button>
            <button type="button" onclick="window.location.href='/dashboard/professor'" class="btn-cancel">Cancelar</button>
        </div>
    </form>
</div>
