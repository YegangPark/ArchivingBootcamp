from django.contrib import admin
from .models import Topic, Lecture, Timestamp, Lecturer

# ① Timestamp를 Lecture 안에서 인라인으로 편집
class TimestampInline(admin.TabularInline):
    model = Timestamp
    extra = 1          # 새 타임스탬프 인스턴스가 몇 개 보일지

# ② Lecture 전용 Admin
@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = (
        'lecture_title',
        'display_lecturers',
        'lecture_date',
        'lecture_length',
    )
    readonly_fields = ('lecture_length',)
    list_filter = ('lecture_date', 'lecture_topics')    
    search_fields = ('lecture_title', 'lecturers__name')        
    filter_horizontal = ('lecture_topics', 'lecturers')              # 다대다 토픽 편집
    inlines = [TimestampInline]                          # ① 등록한 인라인

    def display_lecturers(self, obj):
        """Comma‑separated list of lecturers."""
        return ", ".join([lect.name for lect in obj.lecturers.all()])

    display_lecturers.short_description = 'Lecturers'

# ③ Topic 전용 Admin
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# ④ Timestamp 단독 편집도 필요하다면
@admin.register(Timestamp)
class TimestampAdmin(admin.ModelAdmin):
    list_display = ('lecture', 'label', 'time')
    list_filter = ('lecture',)
    search_fields = ('label',)

@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', )
