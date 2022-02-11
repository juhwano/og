// 식별용 index
let choice_idx = 0
let select_idx = 0
// 문항 추가
const addChoice = () => {
    let new_choice_div = document.querySelector('#new_choice_div')
    // div
    let new_choice = document.createElement('div')
    let div_tag = document.createElement('div')
    let new_select_div = document.createElement('div')
    // input
    let choice_input = document.createElement('input')
    let select_input = document.createElement('input')
    // btn
    let select_add_btn = document.createElement('button')
    let choice_del_btn = document.createElement('button')
    // br
    let br_tag1 = document.createElement('br')
    let br_tag2 = document.createElement('br')
    let br_tag3 = document.createElement('br')
    let br_tag4 = document.createElement('br')
    // hr
    let hr_tag = document.createElement('hr')
    // select
    let select_type = document.createElement('select')
    select_type.id = 'selectId'
    select_type.name = 'input[select_type_name]'

    option_list = [{
        'value': 'checkbox',
        'text' : '체크박스',
    },{
        'value': 'radio',
        'text' : '라디오',
    },{
        'value': 'select',
        'text' : '셀렉트',
    }]
    // option
    for (let i in option_list){
        let option = document.createElement('option')
        option.value = option_list[i].value;
        option.text = option_list[i].text;
        select_type.appendChild(option);
    }
    // element settings
    new_choice.id=`new_choice_${choice_idx}`
    new_choice.setAttribute('data-new-choice-index',`${choice_idx}`)
    new_select_div.id = `new_select_div_${choice_idx}`
    choice_input.setAttribute('type','text')
    choice_input.setAttribute('value','문항명')
    choice_input.setAttribute('name','input[choice_name]')
    select_input.setAttribute('type','text')
    select_input.setAttribute('value','선택지명')
    select_input.setAttribute('data-select-name-input-index',`${choice_idx}`)
    select_input.setAttribute('disabled','disabled')
    select_add_btn.setAttribute('type','button')
    select_add_btn.setAttribute('class','btn btn-sm btn-info')
    select_add_btn.setAttribute('id','select_add_btn')
    select_add_btn.setAttribute('data-add-select-index',`${choice_idx}`)
    select_add_btn.setAttribute('onclick','addSelect(this)')
    choice_del_btn.setAttribute('type', 'button')
    choice_del_btn.setAttribute('class','btn btn-sm btn-danger')
    choice_del_btn.setAttribute('id','choice_del_btn')
    choice_del_btn.setAttribute('data-del-choice-index', `${choice_idx}`)
    choice_del_btn.setAttribute('onclick', 'removeChoice(this)')
    select_add_btn.innerText = '선택지 추가'
    choice_del_btn.innerText = '문항 삭제'
    // add DOM
    // 문항명
    new_choice.appendChild(choice_input)
    new_choice.appendChild(br_tag1)
    // 선택지명
    new_choice.appendChild(select_input)
    new_choice.appendChild(select_add_btn)
    new_choice.appendChild(new_select_div)
    new_choice.appendChild(br_tag2)
    // 선택지 유형 선택
    new_choice.appendChild(select_type)
    new_choice.appendChild(br_tag3)
    // 선택지 추가
    new_choice.appendChild(div_tag)
    new_choice.appendChild(br_tag4)
    // 문항 삭제
    new_choice.appendChild(choice_del_btn)
    new_choice.appendChild(hr_tag)
    // 부모 div
    new_choice_div.appendChild(new_choice)

    choice_idx += 1
}
// 문항 삭제
const removeChoice = (event) => {
    let btn_index = event.dataset.delChoiceIndex
    let parent = document.querySelector('#new_choice_div')
    let child = document.querySelector(`#new_choice_${btn_index}`)
    parent.removeChild(child)
}
// 선택지 추가
const addSelect = (event) => {
    let btn_index = event.dataset.addSelectIndex

    let select_div = document.querySelector(`#new_select_div_${btn_index}`)
    let new_select = document.createElement('input')
    new_select.setAttribute('type','text')
    new_select.setAttribute('id',`select_name_${select_idx}`)
    new_select.setAttribute('name','input[select_name]')
    new_select.setAttribute('data-select-name-idx', `${select_idx}`)
    let select_del_btn = document.createElement('button')
    let select_br = document.createElement('br')
    select_br.setAttribute('id', `select_br_${btn_index}`)
    select_del_btn.setAttribute('type','button')
    select_del_btn.setAttribute('id',`select_del_btn_${select_idx}`)
    select_del_btn.setAttribute('class','btn btn-sm btn-danger')
    select_del_btn.setAttribute('onclick', 'removeSelect(this)')
    select_del_btn.setAttribute('data-select-del-btn-idx', `${select_idx}`)
    select_br.setAttribute('id',`select_br_${select_idx}`)
    select_del_btn.innerText = '선택지 삭제'

    select_div.appendChild(new_select)
    select_div.appendChild(select_del_btn)
    select_div.appendChild(select_br)

    select_idx += 1
}
// 선택지 삭제
const removeSelect = (event) => {
    let btn_index = event.dataset.selectDelBtnIdx

    let del_select_btn = document.querySelector(`#select_del_btn_${btn_index}`)
    let del_select_input = document.querySelector(`#select_name_${btn_index}`)
    let del_select_br = document.querySelector(`#select_br_${btn_index}`)
    let parent = del_select_btn.parentNode
    parent.removeChild(del_select_btn)
    parent.removeChild(del_select_br)

    del_select_input.parentNode.removeChild(del_select_input)

}