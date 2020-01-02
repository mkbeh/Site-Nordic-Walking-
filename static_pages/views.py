from django.shortcuts import render


static_pages = {
    # Section: About federation
    'goals': 'static_pages/goals.html',
    'tasks': 'static_pages/tasks.html',
    'composition': 'static_pages/composition.html',
    'structure': 'static_pages/structure.html',
    'founding_documents': 'static_pages/foundingDocuments.html',

    # Section: Sport
    'protocols': 'static_pages/protocols.html',
    'judges': 'static_pages/judges.html',
    'rules': 'static_pages/rules.html',

    # Contacts
    'contacts': 'static_pages/contacts.html',

    # Donate
    'donate': 'static_pages/donate.html'
}


def static_page(request, page_name):
    current_page = static_pages.get(page_name)
    return render(request, current_page)
