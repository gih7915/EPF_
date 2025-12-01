% rebase('layout', title='Meu Perfil', nav_dict=nav_dict)

<div class="titulo">
    <h1>Meu Perfil</h1>
    <p>Verifique suas informações</p>
</div>

<div class="card">
    <div class="card-header">
        <div>
            <h3 class="card-title">Minhas Informações</h3>
        </div>
    </div>
    <div class="card-body">
        <p><strong>Nome:</strong> {{aluno.name}}
        <button class="open-modal" id="openModal" modal-id="nome">✏️</button></p>
        <p><strong>Matrícula:</strong> {{aluno.matricula}}
        <button class="open-modal" id="openModal" modal-id="matrícula">✏️</button></p>
        <p><strong>Email:</strong> {{aluno.email}}
        <button class="open-modal" id="openModal" modal-id="email">✏️</button></p>
        <p><strong>Curso:</strong> {{aluno.curso}}
        <button class="open-modal" id="openModal" modal-id="curso">✏️</button></p>
        <p><strong>Data de Nascimento:</strong> {{aluno.birthdate}}
        <button class="open-modal" id="openModal" modal-id="birthdate">✏️</button></p>
    </div>
</div>

<div class="modal" id="nome">
    <div class="modal-inner">
        <form action="/meu_perfil?aluno_id={{aluno.id}}" method="post" class="form-container">
            <div class="form-group">
                <label for="name">Nome:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-actions">
                <button type="submit" class="btn-submit">Concluir</button>
                <button class="close-modal btn-cancel">Cancelar</button>
            </div>
        </form>
    </div>
</div>

<div class="modal" id="matrícula">
    <div class="modal-inner">
        <form action="/meu_perfil?aluno_id={{aluno.id}}" method="post" class="form-container">
            <div class="form-group">
                <label for="matricula">Matrícula:</label>
                <input type="text" id="matricula" name="matricula" required>
            </div>
            <div class="form-actions">
                <button type="submit" class="btn-submit">Concluir</button>
                <button class="close-modal btn-cancel">Cancelar</button>
            </div>
        </form>
    </div>
</div>

<div class="modal" id="email">
    <div class="modal-inner">
        <form action="/meu_perfil?aluno_id={{aluno.id}}" method="post" class="form-container">
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-actions">
                <button type="submit" class="btn-submit">Concluir</button>
                <button class="close-modal btn-cancel">Cancelar</button>
            </div>
        </form>
    </div>
</div>

<div class="modal" id="birthdate">
    <div class="modal-inner">
        <form action="/meu_perfil?aluno_id={{aluno.id}}" method="post" class="form-container">
            <div class="form-group">
                <label for="birthdate">Data de Nascimento:</label>
                <input type="date" id="birthdate" name="birthdate" required>
            </div>
            <div class="form-actions">
                <button type="submit" class="btn-submit">Concluir</button>
                <button class="close-modal btn-cancel">Cancelar</button>
            </div>
        </form>
    </div>
</div>

<div class="modal" id="curso">
    <div class="modal-inner">
        <form action="/meu_perfil?aluno_id={{aluno.id}}" method="post" class="form-container">
            <div class="form-group">
                <label for="curso">Curso:</label>
                    <select id="curso" name="curso" required>
                        <option value="" disabled selected>Selecione um curso</option>
                        % for i in cursos:
                            <option value="{{i}}">{{i}}</option>   
                        % end
                    </select>
            </div>
            <div class="form-actions">
                <button type="submit" class="btn-submit">Concluir</button>
                <button class="close-modal btn-cancel">Cancelar</button>
            </div>
        </form>
    </div>
</div>