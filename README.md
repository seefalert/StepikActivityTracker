<div class="markdown prose w-full break-words dark:prose-invert light"><h2>StepikActivityTracker</h2><p>StepikActivityTracker (Трекер активности на Stepik) - это проект, предназначенный для отслеживания и анализа активности пользователя на платформе Stepik. Этот трекер позволяет собирать информацию о вашем прогрессе, количестве решенных задач и дате их выполнения.</p><h3>Как работает</h3><p>StepikActivityTracker использует Selenium и браузер Firefox для автоматического доступа к вашему профилю на Stepik и сбора данных активности. Программа просматривает таблицу активности и извлекает информацию из каждой ячейки, включая дату и количество решенных задач. Затем полученные данные сохраняются в текстовый файл в формате JSON.</p><h3>Установка и настройка</h3><ol><li><p>Установите Python, если его еще нет на вашем компьютере.</p></li><li><p>Установите необходимые зависимости, выполнив следующую команду:</p><pre><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>shell</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-shell">pip install selenium
</code></div></div></pre></li><li><p>Скачайте WebDriver для браузера Firefox (geckodriver) и установите его. Убедитесь, что путь к драйверу Firefox указан в переменной <code>driver_path</code> в файле <code>stepik_activity_tracker.py</code>.</p></li><li><p>Замените значение переменной <code>stepik_id</code> в файле <code>stepik_activity_tracker.py</code> на свой собственный идентификатор пользователя Stepik.</p></li><li><p>Запустите программу <code>stepik_activity_tracker.py</code> для запуска трекера активности на Stepik.</p></li></ol><h3>Результаты</h3><p>После выполнения программы <code>stepik_activity_tracker.py</code> данные активности будут сохранены в текстовом файле <code>data.txt</code>. Каждая запись будет содержать дату и количество решенных задач. Файл <code>data.txt</code> будет автоматически создан в директории, где находится скрипт <code>stepik_activity_tracker.py</code>. Если файл уже существует, новые данные будут добавлены в конец файла.</p><h3>Отказ от ответственности</h3><p>StepikActivityTracker разработан только для личного использования и соблюдает правила использования платформы Stepik. Однако, использование данного трекера может подпадать под ограничения или политики Stepik. Пользователь несет ответственность за использование данного инструмента и должен соблюдать правила и политики Stepik.</p><h3>Лицензия</h3><p>StepikActivityTracker распространяется под лицензией <a href="https://opensource.org/licenses/MIT" target="_new">MIT</a>. Вы можете свободно использовать, изменять и распространять данный проект в соответствии с условиями указанной лицензии.</p></div>
